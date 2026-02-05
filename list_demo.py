# list = ['trek','cannondale','redline','speclizebike']
# print(list)
#
# print(list[0])
# print(list[-1])
# print(list[1:3])
# message = f'my friend`s bike is {list[-2]}'
# print(message)
from string_demo import message

# list.pop()
# print(list) #['trek', 'cannondale', 'redline']

# 推出坐标为2的值
# list.pop(2)
# print(list) #['trek', 'cannondale', 'speclizebike']
#  添加值
# list.append('jack')
# print(list) #['trek', 'cannondale', 'redline', 'speclizebike', 'jack']

# 当list.length<赋值的下标时，python会报错：list assignment index out of range，超出list参数的坐标
# list[4] = 'banana'
# print(list)

# insert 第一个参数为坐标值，第二个参数为要插入的元素值
# list.insert(2,'banana')
# print(list) #['trek', 'cannondale', 'banana', 'redline', 'speclizebike']

# 当只有值没有坐标值时，报错insert expected 2 arguments, got 1，说明insert值为必须的
# list.insert('apple')
# print(list)

# 删除后的值不会在任何地方再次用到，就用del，否则还是用pop方法 接收被删除的值
# del list[0]
# print(list)  #['cannondale', 'banana', 'redline', 'speclizebike']

# 根据值删除
# list.remove('banana') #['trek', 'cannondale', 'redline', 'speclizebike']
# print(list)



list = ['alice','jack','tom','sam']
invite_message = f'I want to invite {list[0].title()}、{ list[1].title()}、{list[2].title()} to my party'
print(invite_message)
list.insert(2,'amy')
invite_message = f'I want to invite {list[0].title()}、{ list[1].title()}、{list[2].title()} {list[3].title()} to my party'
print(invite_message)

center = len(list) / 2
if len(list) % 2 != 0: center_index = int(center - 0.5)
print(center_index)

list.insert(int(len(list) / 2),'mark')
print(list)

list.append('jerry')
print(list)

people_names=''
for item in list: people_names = people_names + f'{item.title()} '

invite_message = f'I want to invite {people_names} to my party'
print(invite_message)

invite_message = 'I just invite two persons to my party because my table cannot reach here at that time'
print(invite_message)
print(list)

# for item in list:
#     if len(list) >= 2:
#         list.pop()
#         print(list) #['alice', 'jack', 'mark']

# while len(list) > 2:
#     list.pop()
# print(list)
#
# del list[0]
# invite_message = f'I want to invite {list[0]} to my party'
# print(invite_message)

# sort永久性排序
# list.sort()
# print(list)
list.sort(reverse=True)
print(list)
# sorted
print('Here is the origin list:')
print(list)

print('Here is the sorted list:')
print(sorted(list))

print('Here is the original list again:')
print(list)

travel_list = ['yunnan','guangxi','fujian','guangzhou','haerbin','xinjiang']
# travel_list.sort()
print(sorted(travel_list))
print(travel_list)
travel_list.reverse()
print(travel_list)
travel_list.reverse()
print(travel_list)
travel_list.sort()
print(travel_list)
travel_list.sort(reverse=True)
print(travel_list)
print(f'i want to go {len(travel_list)} places')