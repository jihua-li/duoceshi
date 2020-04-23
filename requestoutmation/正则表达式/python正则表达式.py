#1.常见匹配模式
'''
\w 匹配字母数字记下滑线
\W 匹配非字母数字下滑线
\s 匹配任意空白字符，等价于[\t\n\r\f]
\S 匹配任意非空字符
\d 匹配任意数字，等价于[0-9]
\D 匹配任意非数字
\n 匹配一个换行符
^ 匹配字符串的开头
$ 匹配字符串的结尾
. 匹配任意字符，除了换行符，当re.DOTALL被标记时，则可以匹配包括换行符在内的任意字符
* 匹配0个或多个的表达式
+ 匹配一个或多个的表达式
？匹配0个或1个由前面由前面的正则表达式定义的片段，非贪婪模式

'''

# re模块，
#r.match()  -->尝试从字符串的起始位置匹配一个模式，如果 不是起始位置匹配成功的话，match()就返回 none。
# re.match(pattern, string, flags=0)
#贪婪模式.*，非贪婪模式.?，.代表任意字符，尽可能是用非贪婪模式.*?
#匹配换行

#最常规匹配
import re
# content = 'Hello 123 4567 World_This is a Regex Demo'
# # 逐个精确匹配 和 指定{10}精确匹配
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
# print(result)
# print(result.group())
# print(result.span())

#范匹配
# content1 = 'Hello 123 4567 World_This is a Regex Demo'
# result1 = re.match('^Hello.*Demo$', content1)
# print(result1)
# print(result1.group())
# print(result1.span())

#匹配目标
# content2 = 'Hello 1234567 World_This is a Regex Demo'
# #用括号标记匹配的目标，\d+表示至少一个数字
# result2 = re.match('^Hello\s(\d+)\sWorld.*Demo$', content2)
# print(result2)
# print(result2.group(1))
# print(result2.span())

#贪婪匹配
content3 = 'Hello 1234567 World_This is a Regex Demo'
result3 = re.match('^He.*(\d*).*Demo$', content3)
print(result3)
print(result3.group(1))

#非贪婪匹配
# content4 = 'Hello 1234567 World_This is a Regex Demo'
# result4 = re.match('^He.*?(\d+).*?Demo$', content4)
# print(result4)
# print(result4.group(1))
# print(result4.span())

#匹配模式
# content5 = '''Hello 1234567 World_This
#            is a Regex Demo'''
#
# #re.S表示包含换行符
# result5 = re.match('^He.*?(\d+).*?Demo$',content5, re.S)
# # result5 = re.match('^He.*?(\d+).*?Demo', content5) #不用\n, 也不传re.S, 会报错
# print(result5)
# print(result5.group(1))
# print(result5.span())
# print(type(content5))

#转译
# content6 = 'price is $5.00'
# result6 = re.match('price is \$5\.00', content6)
# print(result6)
# print(result6.group())
# print(result6.span())


#总结，尽量使用泛匹配，使用括号得到匹配目标，尽量使用非贪婪模式，换行使用re.S

#>>>>>>>>>>>>>>>>>>>>>------------------->>>>>>>>>>>>>>>>>>#

#r.search() --》re.search 扫描整个字符 并返回第一个成功的匹配。
import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

result = re.search('<li\sdata-view="7".*?singer="(.*?)">(.*?)</a>', html, re.S)
# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(result.group(1),result.group(2))

#总结:为匹配方便，能用search就不用 match
#<<<<<<<<<<<<<<<<------>>>>>>>>>>>>>>>>>>>


#re.findall() -->搜索字符串，以列表形式返回全部能匹配的子串。

html1 = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html1, re.S)
# print(results)
# print(type(results))
for result in results:
    # print(result)
    print(result[0],result[1],result[2])

a = ('/2.mp3', '任贤齐', '沧海一声笑')
print(a[0],a[1],a[2])
# for i in a:
#     print(a[0],a[1],a[2])

#re.sub() 正则替换，替换字符串中每一匹配的子串返回替换后的字符串； result.strip()也可以达到相同的效果
# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings' # 第 个参数:正则匹配的对象
# # 第 个参数:要替换成为的新对象
# # 第三个参数:原字符
# # 把数字全部替换成空
# content = re.sub('\d+', '', content)
# print(content)

#re.compile() 把正则字符串编译成正则表达式对象，多处使用正表的表达式可以使用
content = '''Hello 1234567 World_This
is a Regex Demo'''
pattern = re.compile('He.*?(\d+).*?Demo', re.S)
result7 = re.findall(pattern, content)
print(result7)
#课后练习：取模版页面的内容
