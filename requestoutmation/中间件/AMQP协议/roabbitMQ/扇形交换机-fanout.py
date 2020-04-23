
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

