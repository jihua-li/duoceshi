import logging, json, msgpack
from kafka import KafkaProducer

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')

#连接服务器,这里是单机部署，如果是集群部署需要把不同的服务器都加上
producer = KafkaProducer(
    bootstrap_servers=['111.229.87.152:9092'],
    key_serializer=str.encode,
    value_serializer=msgpack.dumps
)

# 1. topic参数，必须指定
# 2. key:必须bytes类型，可以不指定，但和value必须指定一个，默认None
# 3. value:必须bytes类型，可以不指定，但和value必须指定一个，默认None
future = producer.send('topic_lijihua', key='', value={"name": "黎记化"}, partition=0)

#等待消息发送，超时时间为15秒
result = future.get(timeout=15)

#打印详情
logging.info(result)