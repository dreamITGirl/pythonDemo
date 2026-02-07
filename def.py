# 函数
# 引入的方法
from pringting_model import pringting_model as pm
pm('world')
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
def move(n,a,b,c):
    if n == 1:
        print(f'move {a} to {c}')
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(4,'A','B','C')









# def display_message():
#     print('I am learning functions')
# display_message()
#
# def favourite_book(title):
#     print('One of my favourite books is',title)
#
# favourite_book('世界金融史')

# def make_shirt(size,text):
#     print(f'size:{size},text:{text}')
# make_shirt('XL','nb')
#
# def make_shirt(size='L',text='I love Python'):
#     print(f'size:{size},text:{text}')
# make_shirt('xl')
# make_shirt('l')
# make_shirt(text='logo')


# def describe_city(city,country='China'):
#     print(f'{city} is in {country}')
# describe_city('上海')
# describe_city('北京')
# describe_city('东京','日本')

# def city_country():
#     city = input('请输入一个城市')
#     country = input('请输入这个城市所在的国家')
#     return f'{city},{country}'
# count = 0
# while count < 3:
#     print(city_country())
#     count += 1
#

# def make_album(singer,album,num_songs=None):
#     if num_songs:
#         return {'singer':singer.title(),'album':album,'num_songs':num_songs}
#     else:
#         return {'singer':singer.title(),'album':album}
#
# print(make_album('周杰伦','爱在西元前',10))
# print(make_album('鞠婧祎','恋爱告急'))

# count = 0
# def make_album():
#     singer = input('请输入歌手名称')
#     album = input('请输入该歌手的专辑名称')
#     return f'歌手:{singer},专辑:{album}'
#
# while count < 3:
#     print(make_album())
#     count+=1

# mes_list = ['hello','你好','你叫啥']
# sent_mes = []
# def show_messages(mes_list):
#     for mes in mes_list:
#         print(mes)
#
# show_messages(mes_list)

# def send_messages(mes_list):
#     while len(mes_list):
#         mes = mes_list.pop()
#         print(mes)
#         sent_mes.append(mes)
#
# # send_messages(mes_list)
# send_messages(mes_list[:])
# print(mes_list)
# print(sent_mes)

# def sandwich_maker(*foods):
#     print('用户需要的三明治食材有:')
#     for food in foods:
#         print(f'- {food}')
#
# # 调用函数三次，每次提供不同数量的实参
# sandwich_maker('土豆', '牛肉')
# sandwich_maker('鸡肉', '生菜', '番茄')
# sandwich_maker('火腿', '奶酪', '洋葱', '黄瓜')

# def make_car(manufacturer,model,**car_info):
#     car_info['manufacturer'] = manufacturer
#     car_info['model'] = model
#     return car_info
# print(make_car('subaru','outback',color='blue',tow_package=True))


