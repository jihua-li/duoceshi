

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
def callback(ch, method, properties, body):
    print("获取消息：{}".format(body))

#获取列队名
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue
print(queue_name)
# 循环绑定routing key
binding_keys = ["topic.routing.lijihua1", "topic.routing.lijihua2"]
# binding_keys = ["topic.routing.lijihua*"]
for binding_key in binding_keys:
    channel.queue_bind(
        exchange="ex.topic.lijihua",
        queue=queue_name,
        routing_key=binding_key,
    )
#监听消息列队
channel.basic_consume(on_message_callback=callback, queue=queue_name, auto_ack=False)

print("等待消息 CTRL+C强制退出")

#启动监听
channel.start_consuming()
