# 输入
prompt = 'Please enter your name'
name = input(prompt)
print(f'Hello,{name}')

prompt = 'if you tell us who you are, we can personalize the message you see'
prompt+= '\nWhat is your name?'
name = input(prompt)
print(f'Hello,{name}')

prompt = 'can you tell me your age?'
age = int(input(prompt))
if age >= 18:
    print('you are old enough to vote')
else:
    print('you are not old enough to vote')

prompt = 'please input what cars you want to rent?'
car = input(prompt)
print(f'Let me see if I can find you a {car}')

prompt = 'how many people have a dinner?'
num_people = int(input(prompt))
if num_people > 8:
    print('you need to wait')
else:
    print('you can eat in the table')

prompt = 'enter a number,and I will tell you whether the number % 10 = 0'
name = int(input(prompt))
if name % 10 == 0:
    print('the number % 10 = 0')
else:
    print('the number % 10 != 0')

prompt = '请输入披萨配料'
toppings = ''
while True:
    toppings = input(prompt)
    if toppings == 'quit':
        break
    print(f'I will add {toppings} to your pizza')
print('you can exit')

prompt = 'Please tell me your age?'
age = 0
while age != 'quit':
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print('the ticket is free')
    elif age < 12:
        print('the ticket is $10')
    else:
        print('the ticket is $15')

sandwich_orders = ['tuna','beef','chicken']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich} sandwich')
    finished_sandwiches.append(sandwich)
print(f'these are the finished_sandwiches:{finished_sandwiches}')

sandwich_orders = ['tuna','beef','chicken','tuna','tuna','pig','tuna','chicken']

while 'tuna' in sandwich_orders:
    sandwich_orders.remove('tuna')
print(sandwich_orders)

place_list = []
prompt='If you could visit one place in the world,where would you go?'
place = input( prompt)

while place != 'quit':
    place_list.append(place)
    place = input(prompt)
print(place_list)