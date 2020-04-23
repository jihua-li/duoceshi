import logging
from kafka import KafkaConsumer, TopicPartition

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')

consumer = KafkaConsumer(
    group_id='group2',
    bootstrap_servers=['111.229.87.152:9092'],
)

#指定分区partition=0
tp = TopicPartition('msgTopic', 0)
#初始化
consumer.assign([tp])
#寻找分区的最早可用的偏移量
consumer.seek_to_beginning()
#指定偏移量
consumer.seek(tp, 143)
try:
    for msg in consumer:
        logging.info('[当前接收到的数据为]：{}'.format(msg))
        logging.info('[消息内容]：{}'.format(msg.value))
        logging.info('[当前订阅的topic]: {}'.format(consumer.subscription()))
        logging.info('[当前topic和分区信息]：{}'.format(consumer.assignment()))
        logging.info('[可消费的偏移量]：{}'.format(consumer.beginning_offsets(consumer.assignment())))
except Exception as err:
    logging.info(err)