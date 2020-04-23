import logging, pika, json
from pytest_commons.tsms_redis import TsmsRedis

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')

mq_config = {
    "user": "admin",
    "passwd": "admin",
    "host": "192.168.0.180",
    "port": 5672,
    "vhost": "admin",
}

mq_push = {
    "direct": {
        "queue": "queue.lijihua",
        "exchange": "ex.lijihua",
        "routing_key": "routing.lijihua"
    },
    "fanout": {
        "exchange": "ex.fanout.lijihua",
        "routing_key": "",
        "queue": ["queue.fanout.lijihua1", "queue.fanout.lijihua1"]
    }
}

def write_mq_to_redis(uuid, body):
    """将mq结果写到redis"""
    tr = TsmsRedis()
    res = tr.set_mq(uuid, body)
    if not res:
        logging.error('[mq数据写入到redis失败] {}'.format(body))
        return False
    else:
        return True

class MQPush(object):

    def __init__(self):
        self._host = mq_config.get("host")
        self._port = mq_config.get("port")
        self._vhost = mq_config.get("vhost")
        self._credentials = pika.PlainCredentials(mq_config.get("user"), mq_config.get("passwd")) #声明鉴权信息
        self._connection = None

    def connect(self):
        """与MQ创建连接"""
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self._host,
                port=self._port,
                virtual_host=self._vhost,
                credentials=self._credentials,
            )
        )

    def push_direct(self, body):
        """直连交换机，生产者"""
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

    def push_fanout(self, body):
        """扇形交换机，生产者"""
        if not self._connection:
            return
        exchange = mq_push.get("fanout").get("exchange")
        routingkey = ''
        logging.info("[push fanout config is]: {} {}".format(exchange, routingkey))
        #获取通道
        channel = self._connection.channel()
        #声明交换机
        channel.exchange_declare(exchange=exchange, exchange_type="fanout", durable=True)
        #发送消息
        channel.basic_publish(
            exchange=exchange,
            routing_key=routingkey,
            body=body
        )


    def push_direct_secure(self, body):
        """直连交换机，创建连接，写入信息到列队，安全关闭连接"""
        self.connect()
        self.push_direct(body)
        self.close()

    def push_fanout_secure(self, body):
        """扇形交换机，创建连接，写入信息到列队，安全关闭连接"""
        self.connect()
        self.push_fanout(body)
        self.close()

    def consume_direct(self):
        """消费直连交换机列队信息"""
        if not self._connection:
            return
        logging.info("[开始消费]")
        queue = mq_push.get("direct").get("queue")
        channel = self._connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        channel.basic_consume(on_message_callback=self.callback, queue=queue, auto_ack=True)
        channel.start_consuming()

    @staticmethod
    def callback(ch, method, properties, body):
        """回调函数，作为consume_direct函数中channnel.basic_consume()方法的参数"""
        logging.info("[ch is]: {}".format(ch))
        logging.info("[methos is]: {}".format(method))
        logging.info("[properties is]: {}".format(properties))
        logging.info("[body is]: {}".format(body))
        logging.info(type(json.loads(body.decode())))
        uuid = json.loads(body.decode())['uuid']
        logging.info('开始写入redis')
        write_mq_to_redis(uuid, body.decode())


    def close(self):
        """关闭MQ连接"""
        if self._connection:
            self._connection.close()


if __name__ == '__main__':
    mq = MQPush()
    data = {"uuid": "a1e2ff2e-23c5-11ea-a694-acde48001122", "phone": "17134198056", "content": "【hellokitty】验证码为：123"}
    # mq.push_direct_secure(json.dumps(data))
    # mq.push_fanout_secure(json.dumps(data))
    mq.connect()
    # mq.push_direct("hello")
    # mq.close()
    mq.consume_direct()
