import pika, random, sys

#声明签名信息
credentials = pika.PlainCredentials("admin", "admin")
#创建连接
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="192.168.0.101",
        port=5672,
        virtual_host="admin",  # 指定虚拟机
        credentials=credentials
    )
)
#建立通道
channel = connection.channel()


"""发布者"""

# message = ' '.join(sys.argv[1:]) or 'hello dsc !'
#
# #声明交换机
# channel.exchange_declare(exchange="lijihua.logs", exchange_type="fanout", durable=True)
#
# # 使用由空字符串表示的默认交换机即可
# # 默认交换机比较特别，它允许我们指定消息究竟需要投递到哪个具体的队列中，队列名字需要在 routing_key参数中指定
# channel.basic_publish(exchange="lijihua.logs", routing_key='', body=message.encode())
#
# print("发送消息：{}".format(message))
#
# #安全关闭连接
# channel.close()


'''订阅者'''
#声明交换机
channel.exchange_declare(exchange="lijihua.logs", exchange_type="fanout", durable=True)
# 定义随机队列，传空，即随机生成，exclusive=True 表示消费者断开后，即删除队列
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

#绑定列队交换机
channel.queue_bind(exchange="lijihua.logs", queue=queue_name)

def callback(hc, method, properties, body):
    print("获取消息内容：{}".format(body))

#监听消息列队,ack为True, 有回执,则认定消费成功，会删除掉MQ中的数据
channel.basic_consume(on_message_callback=callback, queue=queue_name, auto_ack=False)

#启动监听
channel.start_consuming()