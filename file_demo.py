# with  open('./static/file.txt') as f:
#     # 直接读取
#     content = f.read()
#     print(content.rstrip())
    # 逐行读取
    # for line in f:
    #     print(line.strip())
from curses.ascii import isdigit


# 写入文件
# with open('./static/file1.txt','w') as f:
#     f.write('I love Python')
#     f.write('\nI love C++')
#     f.write('\nI love Java')

# 练习
def user_name():
    prompt = 'Please enter your name'
    name = input(prompt)
    with open('./static/user.txt','w') as f:
        f.write(f'用户名为{name}')

# user_name()

def greet_guest():
    prompt = 'Please enter your name'
    name=input(prompt)
    with open('./static/guest.txt','a') as f:
        f.write(f'hello,{name}\n')

# greet_guest()

def reason_coding():
    while True:
        prompt = 'Why do you like coding?'
        reason = input( prompt)
        with open('./static/reason.txt','a') as f:
            f.write(f'{reason}\n')
        repeat = input('Do you want to add another reason?(y/n)')
        if repeat != 'y':
            break
# reason_coding()

# 检查两个输入参数是否都是数字字符串
        # isdigit() 最常用
        # 更广义的“数字”判断
        # isnumeric()
        # 最严格的十进制数字判断
        # isdecimal()
# def add_numbers(num1,num2):
#     try:
#         # if num1.isdigit() and num2.isdigit():
#             num = int(num1) + int(num2)
#             print(num)
#     except ValueError:
#
#         print('请输入数字')

# add_numbers('1','2')
# add_numbers('ly','李娅茹')
#
# def add_numbers():
#     while True:
#         try:
#             num1 = input('请输入数字')
#             num2 = input('请输入数字')
#             num = int(num1) + int(num2)
#             print(num)
#             break
#         except ValueError:
#             continue
# add_numbers()

# 读取文件
def read_file(file_path):
    try:
        with open(file_path) as f:
            content = f.read()
            print(content.rstrip())
    except FileNotFoundError:
        print('文件不存在')
# read_file('./static/file.txt')
# read_file('./static/dog.txt')

# 读取文件,静默失败
def read_file_2(file_path):
    try:
        with open(file_path) as f:
            content = f.read()
            print(content.rstrip())
    except FileNotFoundError:
        pass
# read_file_2('./static/file.txt')
# read_file_2('./static/dog.txt')

def count(file_path,key_word):
    try:
        with open(file_path,'r', encoding='utf-8') as f:
            word_count = 0
            content = f.read()
            words = content.split()
            print(words)
            for word in words:
               if word == key_word:
                   word_count += 1
            print(f'{key_word}出现了{word_count}次')
    except FileNotFoundError:
        pass

count('static/上门喂猫服务协议.txt', '')