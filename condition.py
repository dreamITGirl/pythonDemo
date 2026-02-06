car = 'subaru'
if car == 'subaru': print('subaru')
else: print('apple')

print(car == 'apple')

car = 'audi'
print(car == 'audi')

num_sim = [10,20,30]
num_fat = [10,20,30]
print(num_sim == num_fat)

num_sim.append(40)
print(20 in num_sim)

for num in num_sim:
    if num in num_fat:
        print(True)
    else:
        print(False)

for num in num_sim:
    if num in num_fat and num>5:
        print(True)
    else:
        num_fat.append(num)
        print(num)

height = 1.6
weight = 66
bmi = weight/(height**2)
print(bmi)
if bmi<18.5:
    print('过轻')
elif 18.8<=bmi <25:
    print('正常')
elif 25 <=bmi <28:
    print('过重')
elif 28 <=bmi <32:
    print('肥胖')
else :
    print('严重肥胖')

# 联系5.3.1
# alien_color = 'green'
# if alien_color == 'green':
#     print('你获得5分')


# alien_color = 'red'
# if alien_color == 'green':
#     print('你获得5分')
#
# if alien_color == 'green':
#     print('你获得5分')
# else:
#     print('你获得10分')

# alien_color = 'yellow'
# alien_color = 'green'
alien_color = 'red'
if alien_color == 'green':
    print('你获得5分')
elif alien_color == 'yellow':
    print('你获得10分')
elif alien_color == 'red':
    print('你获得15分')


age = 2
if age < 2:
    print('小屁孩')
elif age < 4:
    print('小屁孩')
elif age < 13:
    print('小屁孩')
elif age < 20:
    print('小屁孩')
elif age < 65:
    print('小屁孩')
elif age >= 65:
    print('小屁孩')


fruits = ['purple','banana','pink']
if 'apple' in fruits:
    print('You really like apples')
elif 'banana' in fruits:
    print('You really like bananas')
elif 'orange' in fruits:
    print('You really like oranges')


user_list = ['admin','eric','tom','lucy','jim']
if user_list:
    for user in user_list:
        if user == 'admin':
            print(f'Hello {user}, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in again')

user = 'alice'
if user_list and user in user_list:
    print(f'Hello {user}, thank you for logging in again')
else:
    print('We need to find some users!')
