import records,logging
import config.tsms_db_config as tsms_db_config
import config.tsms_base_config as tsms_base_config
from robot_commons.tsms_decorator import logit

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')

class OperationDb:
    def __init__(self, env = 0):
        self.limit_fileds = tsms_db_config.limit_fileds
        if tsms_base_config.env == 0:
            pass
        elif tsms_base_config.env == 1:
            self.db_config = tsms_db_config.test_db_config
        elif tsms_base_config.env == 2:
            self.db_config = tsms_db_config.pro_db_config
        else:
            self.db_config = tsms_db_config.test_db_config

        self.db_connect_str = 'mysql+{0}://{1}:{2}@{3}:{4}/{5}?charset={6}'.format('pymysql',self.db_config['user'],self.db_config['password'],
                                                                                   self.db_config['host'],self.db_config['port'],
                                                                                   self.db_config['db'],self.db_config['charset'])
        try:
            self.db = records.Database(self.db_connect_str)
        except Exception as err:
            logging.error(err)
            raise
        self.res = ''
    @logit
    def execute_sql(self, sql):
        '''执行sql
            '''
        try:
            res = self.db.query(sql).all(as_dict=True)
            logging.info("[execute result is]:{}".format(res))
            self.res = res[0]
            logging.info('tpye(res):{}, res:{}'.format(type(self.res), res))
            return res
        except Exception as err:
            logging.error(err)
            raise

    @logit
    def tsms_select(self, table_name, *fields, **kwargs):
        '''创建sql并调用执行sql方法execute_sql,返回执行结果
            select *fields from table_name **kwargs
        '''
        options = "where " if kwargs else ""
        for k,v in kwargs.items():
            if isinstance(v, str):
                v = '\"' + v + '\"'
            options += k + "=" + str(v) + " and "
        if kwargs:
            options = options[:-4]
        query_sql = ','.join(fields)
        sql = 'select {0} from {1} {2}'.format(query_sql,table_name, options)
        logging.info("[now execute sql is]:{}".format(sql))
        return self.execute_sql(sql)

    @logit
    def tsms_update(self, table, field, value, **kwargs):
        """更新指定的字段，一次只允许修改一个"""
        # 限制字段["audit_status", "is_delete"]
        if field not in self.limit_fileds:
            logging.error("[更新字段失败]: {}".format(field))
            return
        if kwargs:
            options = 'where '
            for k, v in kwargs.items():
                if isinstance(v, str):
                    v = '\"' + v + '\"'
                options += k + "=" + str(v) + " and "
            options = options[:-4]
        else:
            return
        if isinstance(value, int):
            sql = '''update {0} set {1}={2} {3};'''.format(table, field, value, options)
        else:
            sql = '''update {0} set {1}="{2}" {3};'''.format(table, field, value, options)
        logging.info("[now execute sql is]: {}".format(sql))
        try:
            self.db.query(sql)
        except:
            logging.ERROR("[数据库更新失败 sql 是]: {}".format(sql))

    @logit
    def tsms_record_del(self, table, **kwargs):
        '''软删除表数据'''
        if not kwargs:
            logging.error("删除条件不能为空")
            return
        self.tsms_update(table, "is_delete", 1, **kwargs)

    @logit
    def check_res(self, key, value):
        assert str(self.res[key]) == value



if __name__ =='__main__':
    db = OperationDb()
    res = db.tsms_select('sms_sign',"sign_id,audit_status",sign_user_id = 16,sign_id = 798)
#     print(res)
# db = OperationDb()
# res = db.tsms_select('sms_sign',"sign_id,audit_status",sign_user_id = 16,sign_id = 798)