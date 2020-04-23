import redis



pool = redis.ConnectionPool(host='148.70.194.135', port=6379, password='dcs123', db=0, decode_responses=True)
re_db = redis.Redis(connection_pool=pool)
account = re_db.get("tsms:{}:account".format('dcs'))
print(account)