import tsms_project.config.tsms_redis_config as redis_config
from tsms_project.commons.tsms_decorator import logit
import redis,records,logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')



class TsmsRedis:
    '''redis测试库封装'''
    def __init__(self):
        self.redis_config = redis_config.redis_config
        pool = redis.ConnectionPool(**self.redis_config)
        self.redis_connect = redis.Redis(connection_pool=pool)
    @logit
    def get_account(self, user='lijihua'):
        '''获取充值金额'''
        key = 'tsms:{}:account'.format(user)
        res = self.redis_connect.get(key)
        logging.info("返回内容是：{}".format(res))
        try:
            return int(res)
        except:
            return

    @logit
    def get_freq(self, phone='16627891036'):
        '''获取短信发送频率'''
        key = 'freq:{}'.format(phone)
        freq_res = self.redis_connect.get(key)
        freq_ttl_res = self.redis_connect.ttl(key)
        # try:
        #     return int(freq_res), int(freq_ttl_res)
        # except:
        #     return
        logging.info("{} = {} ttl = {}".format(key, freq_res, freq_ttl_res))
        freq_res_0 = 0
        freq_ttl_res_0 = 0
        if freq_res and freq_ttl_res:
            return int(freq_res),int(freq_ttl_res)
        elif not freq_res and freq_ttl_res:
            return freq_res_0, int(freq_ttl_res)
        elif freq_res and not freq_ttl_res:
            return int(freq_res), freq_ttl_res_0
        elif not freq_res and not freq_ttl_res:
            return freq_res_0,freq_ttl_res_0
        else:
            raise "接口返回结果异常"

    @logit
    def set_freq(self, phone, ttl, value):
        key = 'freq:{}'.format(phone)
        self.redis_connect.setex(key, ttl, value)
        res = self.get_freq(phone)
        freq,ttl = res
        logging.info("now freq is : {}".format(freq))
        return res[0]

    @logit
    def set_account(self, user, money= 0):
        key = 'tsms:{}:account'.format(user)
        res = self.redis_connect.set(key, money)
        logging.info('{} = {}'.format(key, money))
        return res

if  __name__ =='__main__':
    tr = TsmsRedis()
    # print(tr.get_account())
    print(tr.get_freq("16627891036"))
    # freq = tr.set_freq("16627891036", 600, 19)
    # print(freq, type(freq))
    # print(tr.set_account('16627891036'))