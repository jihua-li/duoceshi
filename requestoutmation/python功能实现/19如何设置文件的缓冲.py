"""
将文件内容写入到硬件设备时，使用系统调用，这类I/O操作的时候很长，为了减少I/O操作的次数，
文件通常使用缓冲（有足够多的数据才进行系统调用），文件的缓冲行为，分为全缓冲，行缓冲，无缓冲
"""

#备注：但是目前发现无论哪种设置现在都是立即写入，还不知道原因

#查看python默认写入的缓冲大小

# f = open('demo.txt', 'w')
# f.write('abc')
# f.close()

#全缓冲
f = open('demo1.txt', 'w', buffering=2048)
f.write('+' * 1024)
f.write('*' * 1023)

#行缓冲,buffering设置为1
f = open('demo2.txt', 'w', buffering=1)
f.write('skdjfj\n')

#无缓冲，buffering设置为0
f = open('demo.txt', 'w', buffering=0)
f.write('ds')