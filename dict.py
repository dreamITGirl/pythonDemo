# 字典
friend_info={
    'first_name':'li',
    'last_name':'Alice',
    'age':'34',
    'city:':'shenyang'
}
print(friend_info)

friend_nums={
    'li':'123',
    'alice':'456',
    'tom':'789',
    'lucy':'1011',
    'bob':'2026',
    'jerry':'789'
}

# num = friend_nums.get('bob','no numbers he like')
# num = friend_nums.get('lucy','no numbers he like')
# num = friend_nums.get('tom','no numbers he like')
# num = friend_nums.get('alice','no numbers he like')
# num = friend_nums.get('li','no numbers he like')
# num = friend_nums.get('jd','no numbers he like')
# print(num)

# 遍历
# for name,num in friend_nums.items():
#     print(f'name:{name}',
#           f'\nnumber:{num}')
#     print('name',name,'\nnumber',num)

# 遍历健值对
# for name in friend_nums.keys():
#     print(name)
#
# for num in friend_nums.values():
#     print(num)
list = []
name_list = []
for num in set(friend_nums.values()):
    list.append(num)
    # print(num)
print(list)

for name in sorted(friend_nums.keys()):
    name_list.append( name)
print(name_list)

for name in friend_nums.items():
    if int(name[1]) > 1000:
        print(name[0],'喜欢数字',name[1])
    else :
        print(name[0],'不喜欢数字',name[1])

# 嵌套
# friend_info={
#     'first_name':'li',
#     'last_name':'Alice',
#     'age':'34',
#     'city:':'shenyang'
# }

pepple_list = [
    friend_info,
    {
        'first_name':'jd',
        'last_name':'mary',
        'age':'20',
        'city:':'sanya'
    },
{
        'first_name':'xiaohei',
        'last_name':'sum',
        'age':'30',
        'city':'xiamen'
    },
]

if pepple_list:
    for item in pepple_list:
        for k,v in item.items():
            print(f'{k}:{v}')
else:
    print('没有用户')

pets_list = [
    {
        'pet_name': '豆花儿',
        'pet_type': 'cat',
        'pet_owner': 'li',
        'age': 5
    },
    {
        'pet_name': '安安',
        'pet_type': 'cat',
        'pet_owner': 'alice',
        'age': 3
    },
    {
        'pet_name': '小黑',
        'pet_type': 'dog',
        'pet_owner': 'tom',
        'age': 2
    },
    {
        'pet_name': '小黄',
        'pet_type': 'dog',
        'pet_owner': 'lucy',
        'age': 1
    }
]
if pets_list:
    for pet in pets_list:
        print(f'宠物名字是{pet["pet_name"]}，类型是{pet["pet_type"]}，主人是{pet["pet_owner"]}，年龄是{pet["age"]}')
else:
    print('没有宠物')
