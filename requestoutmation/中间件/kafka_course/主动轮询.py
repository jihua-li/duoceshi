import logging, time
from kafka import KafkaConsumer

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')

consumer = KafkaConsumer(
    'topic_lijihua',
    group_id='group_lijihua',
    bootstrap_servers=['111.229.87.152:9092'],
    # consumer_timeout_msg=1000
)
while True:
    msg = consumer.poll(timeout_ms=10000) #从kafa拉取消息，消息等待间隔10秒
    logging.info('[当前接收到的数据为]：{}'.format(msg))

    for tp, messages in msg.items():
        for message in messages:
            logging.info('{}:{}:{}: key{} value{}'.format(tp.topic, tp.partition, message.offset, message.key, message.value))

    time.sleep(5)


