#通过sys.argv[1:]获取有效参数，通过getopt.getopt()来管理参数
import sys, getopt

#第0个参数就是xx.py本身
# print('全部sys.argv的参数为：', sys.argv)

# 我们需要的参数从1开始，注意:解析出来的是，按照空格隔开的列表
# arguments = sys.argv[1:]
# print('我们需要的参数是：', arguments)

# 通过getopt进行参数管理，接收三个参数:
#  1. 当前脚本的参数
# 2. 短参数
# 3. 长参数

#短参数
#不带值
# arg1 = getopt.getopt(sys.argv[1:], '-h', ['host'])
# print('通过getopt解析结果是：', arg1)

#带值
# arg2 = getopt.getopt(sys.argv[1:], '-h:', ['host'])
# print('通过getopt解析结果是：', arg2)

#长参数
#不带值
# arg3 = getopt.getopt(sys.argv[1:], '-h', ['host'])
# print('通过getopt解析结果是：', arg3)

#带值
# arg4 = getopt.getopt(sys.argv[1:], '-h:', ['host='])
# arg4 = getopt.getopt(sys.argv[1:], '-h:', ['host='])
# print('通过getopt解析结果是：', arg4)


'''案例:脚本可以指定启动地址和监听端口， 如: python py_script_pram_many.py —- host=127.0.0.1 -p 5001'''
host, port = None, None
opts, args = getopt.getopt(sys.argv[1:], '-h:-p:', ['host=', 'post='])
print(opts)
print(args)
for opt_name, opt_value in opts:
    if opt_name in('-h', '--host'):
        host = opt_value
        # print('host address is:', host)

    if opt_name in('-p', '--post'):
        port = opt_value
        # print('port is:', port)
if not host:
    print('host can not null')
    sys.exit(1)
if not port:
    port = 8080

print('host={},port={}'.format(host, port))