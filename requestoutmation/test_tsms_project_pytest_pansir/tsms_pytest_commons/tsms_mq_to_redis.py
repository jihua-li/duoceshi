import logging, pika, json
from tsms_pytest_commons.tsms_rds import TsmsRedis

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')

mq_config = {
    "user": "admin",
    "passwd": "admin",
    "host": "10.211.55.5",
    "port": 5672,
    "vhost": "admin",
}

mq_push = {
    "direct": {
        "queue": "queue.celery.tsms.mq",
        "exchange": "ex_send",
        "routing_key": "routing.tsms.send"
    }
}


def write(key, body):
    """将mq结果写到redis"""
    rds = TsmsRedis()
    res = rds.set_mq(key, body)
    if not res:
        logging.error("[mq数据写入redis失败]: {}".format(body))
        return False
    else:
        return True


class MQPush(object):

    def __init__(self):
        self._host = mq_config.get("host")
        self._port = mq_config.get("port")
        self._vhost = mq_config.get("vhost")
        self._credentials = pika.PlainCredentials(mq_config.get("user"), mq_config.get("passwd"))
        self._connection = None

    def connect(self):
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self._host,
                port=self._port,
                virtual_host=self._vhost,
                credentials=self._credentials,
            )
        )

    def push_direct(self, body):
        if not self._connection:
            return
        queue = mq_push.get("direct").get("queue")
        exchange = mq_push.get("direct").get("exchange")
        routingkey = mq_push.get("direct").get("routing_key")
        logging.info("[push direct config is]: {} {}".format(exchange, routingkey))
        logging.info("[push body is]: {}".format(body))
        # 获取通道
        channel = self._connection.channel()
        # 绑定队列
        channel.queue_declare(queue=queue, durable=True)
        # 发送消息
        channel.basic_publish(
            exchange=exchange,  # 为空也允许
            routing_key=routingkey,
            body=body,
        )

    def push_direct_secure(self, body):
        self.connect()
        self.push_direct(body)
        self.close()

    def consume_direct(self, queue):
        if not self._connection:
            return
        logging.info("[开始消费]")
        channel = self._connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        channel.basic_consume(on_message_callback=self.callback, queue=queue, auto_ack=True)
        channel.start_consuming()

    @staticmethod
    def callback(ch, method, properties, body):
        logging.info("[ch is]: {}".format(ch))
        logging.info("[methos is]: {}".format(method))
        logging.info("[properties is]: {}".format(properties))
        logging.info("[body is]: {}".format(body))
        uuid = json.loads(body.decode())["uid"]
        logging.info("[开始写入redis]")
        write(uuid, body.decode())

    def close(self):
        if self._connection:
            self._connection.close()


if __name__ == '__main__':
    mq = MQPush()
    mq.connect()
    mq.consume_direct("queue.tsms.send")
