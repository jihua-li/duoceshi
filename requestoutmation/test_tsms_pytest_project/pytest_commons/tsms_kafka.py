from kafka import KafkaProducer
from kafka.errors import KafkaError
import logging,json

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')

kfk_config = {
    "host": "111.229.87.152",
    "port": 9092,
}


class KafkaSender:
    def __init__(self, kafkaTopic="topic_dcs"):
        self.kafkaHost = kfk_config.get("host")
        self.kafkaPort = kfk_config.get("port")
        self.kafkaTopic = kafkaTopic
        self.producer = None

    def connect(self):
        self.producer = KafkaProducer(
            bootstrap_servers='{kafka_host}:{kafka_port}'.format(
                kafka_host=self.kafkaHost,
                kafka_port=self.kafkaPort
            )
        )

    def close(self):
        self.producer.close()

    def send_data(self, params):
        logging.info("[现在准备发送数据]: {}".format(params))
        if isinstance(params, dict):
            try:
                params = json.dumps(params)
            except:
                logging.error("[字典格式数据序列化失败！！！]")
        try:
            producer = self.producer
            producer.send(self.kafkaTopic, key=None, value=params.encode('utf-8'))
            producer.flush()
        except KafkaError as e:
            return {"result": "error", "message": str(e)}
        else:
            return {"result": "success", "message": "发送成功"}

    def send_data_secure(self, params):
        self.connect()
        self.send_data(params)
        self.close()


if __name__ == '__main__':
    message = '{"uid": "241214764", "phone": "13988886666", "content": "【nice】hello"}'
    sender = KafkaSender()
    # sender.send_data(message)
    sender.send_data_secure(message)