import random




def func(n):
    if n <= 2:
        return n
    return func(n-1) + func(n-2)


print(func(5))


# name_gift = {'a': 1, 'b': 2, 'c': 3}
# names = []
# gifts = []
# news_name_gift = {}
#
# def get_gift(name_gift):
#     for n, g in name_gift.items():
#         names.append(n)
#         gifts.append(g)
#         print(names,gifts)
#     for i in len(names):
#         name = random.choice(names)
#         gift = random.choice(gifts)
#         news_name_gift['name'] = gift
#         if name_gift['name'] == gift:
#
#
#
#
# get_gift(name_gift)

dictGiftIn = {'Jack': 'apple', 'Peter': 'beer', 'Tom': 'card', 'Duke': 'doll', 'Mary': 'pineapple', 'James': 'flute',
              'Tina': 'coffee'}
dictGiftOut = {}
persons = list(dictGiftIn.keys())
for p in persons:
    flag = 0  # 标记自己带来的礼物是否还未分配出去
    if p in dictGiftIn:
        flag = 1
        myGift = dictGiftIn.pop(p)  # 如果自己带来的礼物还未分配，则去掉该礼物
        print(myGift)
    getGift = dictGiftIn.popitem()  # 随机返回并移除一对key-value值
    print(getGift,type(getGift))
    dictGiftOut[p] = getGift[1]  # 得到的礼物
    if flag:
        dictGiftIn[p] = myGift  # 将自己的礼物添到未分配礼物中

print(dictGiftOut)  # 输出礼物分配情况