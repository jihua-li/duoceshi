import logging, json
from kafka import KafkaConsumer

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')

consumer = KafkaConsumer(
    'topic_lijihua',
    group_id='group_lijihua',
    bootstrap_servers=['111.229.87.152:9092'],
    key_deserializer=bytes.decode,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')) #先解码再反序列化
)
try:
    for msg in consumer:
        logging.info('[当前接收到的数据为]：{}'.format(msg))
        logging.info('[消息内容]：{}'.format(msg.value))
        logging.info('[当前订阅的topic]: {}'.format(consumer.subscription()))
        logging.info('[当前topic和分区信息]：{}'.format(consumer.assignment()))
        logging.info('[可消费的偏移量]：{}'.format(consumer.beginning_offsets(consumer.assignment())))
except Exception as err:
    logging.info(err)


