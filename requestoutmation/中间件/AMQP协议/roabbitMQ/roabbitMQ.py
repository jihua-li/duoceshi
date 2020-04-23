"""
rabbitMQ
    模式：
        1、直连交换机
        2、扇形交换机
        3、主题交换机
        4、头部交换机
    页面解读：

    --发布订阅模式

"""

import pika


"""直连交换机（direct）"""
# 声明鉴权信息
# credentials = pika.PlainCredentials('admin', 'admin')
#
# # 建立与rabbitMQ的连接
# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(
#         host='192.168.0.182',
#         port=5672,
#         virtual_host='admin',
#         credentials=credentials,
#     )
# )
# channel = connection.channel()

"""生产者"""
# 写入信息，其中exchange, routing_key要与上面声明的queue对应
# for i in range(5):
#     channel.basic_publish(
#         exchange='ex.lijihua',
#         routing_key='routing.lijihua',
#         body=b'hello lijihua',
#     )
#
# print('发送一条信息')
#
# #安全关闭连接
# connection.close()



"""消费者"""
# 声明列队并设置为持久化
# channel.queue_declare(queue='queue.lijihua', durable=True)
#
#
# # 为列队定义一个回调函数
# def callback(ch, method, properties, body):
#     print("[x] Received ：%r" % body)
#
#
# # 监听消息队列，ack为False, 没有回执，所以会一直消费，不会删除MQ中的数据
# # channel.basic_consume(on_message_callback=callback, queue='queue.lijihua', auto_ack=False)
# # 监听消息队列，ack为True, 有回执,则认定消费成功，会删除掉MQ中的数据
# channel.basic_consume(on_message_callback=callback, queue='queue.lijihua', auto_ack=True)
#
# print('消息队列监听中....')
#
# # 启动监听
# channel.start_consuming()


"""扇形模式（fanout）"""
import pika, random

'''生产者'''
# #申明鉴权信息
# credentials =pika.PlainCredentials("admin", "admin")
# #与roabbitMQ创建连接
# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(
#         host="192.168.0.101",
#         port=5672,
#         virtual_host="admin", #指定虚拟机
#         credentials=credentials
#     )
# )
# channel = connection.channel()
# #申明交换机
# channel.exchange_declare(exchange="ex.fanout.lijihua", exchange_type="fanout", durable=True)
# a = random.randint(1, 9999)
# msg = "hello word ! {}".format(str(a))
# channel.basic_publish(
#     exchange="ex.fanout.lijihua",
#     routing_key='',
#     body=msg.encode(),
# )
#
# print("发送一条信息！")
#
# connection.close()


'''消费者'''
#
# def callback(ch, method, properties, body):
#     print("获取到列队消息：{}".format(body))
#
# #建立连接1
# channel1 = connection.channel()
# channel1.queue_declare(queue="queue.fanout.lijihua", durable=True)
# channel1.basic_consume(on_message_callback=callback, queue='queue.fanout.lijihua', auto_ack=True)
#
# #建立连接2
# channel2 = connection.channel()
# channel2.queue_declare(queue="queue.fanout.lijihua1", durable=True)
# channel2.basic_consume(on_message_callback=callback, queue='queue.fanout.lijihua1', auto_ack=False)
#
# print('等待消息 CTRL+C强制退出')
# # 运行一个用来等待消息数据并且在需要的时候运行回调函数的无限循环
# channel1.start_consuming()
# channel2.start_consuming()



"""主题交换机-
    同一个消费者可以消费不同队列里面的数据"""

import pika, random

'''生产者'''
#申明鉴权信息
credentials =pika.PlainCredentials("admin", "admin")
#与roabbitMQ创建连接
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="192.168.0.101",
        port=5672,
        virtual_host="admin", #指定虚拟机
        credentials=credentials
    )
)
channel = connection.channel()
#声明交换机
channel.exchange_declare(exchange="ex.topic.lijihua", exchange_type="topic", durable=True)


a = random.randint(1, 9999)
msg = "hello word {} !".format(str(a))
#写第一条
channel.basic_publish(
    exchange="ex.topic.lijihua",
    routing_key="topic.routing._ijihua1",
    body=msg.encode(),
)

#写第二条
channel.basic_publish(
    exchange="ex.topic.lijihua",
    routing_key="topic.routing_lijihua2",
    body=msg.encode(),
)

print("发送两条信息：{}".format(msg))
#安全关闭连接
channel.close()



'''消费者'''
# def callback(ch, method, properties, body):
#     print("获取消息：{}".format(body))
#
# #获取列队名
# result = channel.queue_declare('', exclusive=True)
# queue_name = result.method.queue
# print(queue_name)
# # 循环绑定routing key
# binding_keys = ["topic.routing.lijihua1", "topic.routing.lijihua2"]
#
# for binding_key in binding_keys:
#     channel.queue_bind(
#         exchange="ex.topic.lijihua",
#         queue=queue_name,
#         routing_key=binding_key,
#     )
# #监听消息列队
# channel.basic_consume(on_message_callback=callback, queue=queue_name, auto_ack=False)
#
# print("等待消息 CTRL+C强制退出")
#
# #启动监听
# channel.start_consuming()
