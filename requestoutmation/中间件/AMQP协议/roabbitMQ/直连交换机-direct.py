import pika, random


"""直连交换机（direct）"""
# 声明鉴权信息
credentials = pika.PlainCredentials('admin', 'admin')

# 建立与rabbitMQ的连接
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='192.168.0.182',
        port=5672,
        virtual_host='admin',
        credentials=credentials,
    )
)
channel = connection.channel()

"""生产者"""
# 写入信息，其中exchange, routing_key要与上面声明的queue对应
for i in range(5):
    channel.basic_publish(
        exchange='ex.lijihua',
        routing_key='routing.lijihua',
        body=b'hello lijihua',
    )

print('发送一条信息')

#安全关闭连接
connection.close()



"""消费者"""
# 声明列队并设置为持久化
channel.queue_declare(queue='queue.lijihua', durable=True)


# 为列队定义一个回调函数
def callback(ch, method, properties, body):
    print("[x] Received ：%r" % body)


# 监听消息队列，ack为False, 没有回执，所以会一直消费，不会删除MQ中的数据
# channel.basic_consume(on_message_callback=callback, queue='queue.lijihua', auto_ack=False)
# 监听消息队列，ack为True, 有回执,则认定消费成功，会删除掉MQ中的数据
channel.basic_consume(on_message_callback=callback, queue='queue.lijihua', auto_ack=True)

print('消息队列监听中....')

# 启动监听
channel.start_consuming()