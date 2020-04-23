

# with open('py1.txt', 'wt') as f:
#     f.write('你好')

f = open('test.txt', 'wt', encoding='utf8')
# f.write('你好')
f.write('中国')
f.close()

f = open('test.txt', 'rt', encoding='utf8')
s = f.read()
print(s)