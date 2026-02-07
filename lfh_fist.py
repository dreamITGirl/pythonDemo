
print('I\'m ok.')
print('hello I\'m liyaru')
print('\'\n\\')
# Python还允许用r''表示''内部的字符串默认不转义
print(r'\\你好\\')
print(r'\\\t\\')
# Python允许用'''...'''的格式表示多行内容
print('''line1 
line2 
lin3
''')
print(r'''hello,\n
world''')
print(r''' hello, \n
liyaru''')
# 布尔值：
# 一个布尔值只有True、False两种值
# 布尔值可以用and or not来运算
# and ：是 只有所有都为True，and运算结果才是True
print(True  and True)
print(True and False)
print(5>3 and 3>1)
print(5>3 and 3<1)
# or ：只要有一个为True，or运算结果就是True
print(True or True)
print(True or False)
print(False or False)
# not ：取反 是非运算，它是一个单目运算符，把True变成False，False变成True
print(not True)
print(not False)
print(not 1>2)
age =11
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
# 空值 None None不能理解为0，因为0是有意义的，而None是一个特殊的空值

# 变量 不仅可以是数字，还可以是任意数据类型
num =1
str_01= 'jujingyi'
answer= True
print(num, str_01, answer)
# 在Python中等号=是赋值语句
a= 123
print('a是整数',a)
a='string'
print('a是字符串',a)
# 以上变量本身类型不固定的语言称之为动态语言
# 与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错
# int   b= 123
# b = '123'
# print(b)
# 错误：不能把字符串赋给整型变量


# 常量 ：常量值不能被修改，常量用大写字母表示
# PI = 3.14159265359

# 除法：在Python中，有两种除法
# 一种除法是 / 除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
print(5/2)
# 打印出来的值是 2.5
print(9/3)
# 打印出来的值是 3.0
# 一种除法是//，称为地板除，除法只取结果的整数部分 ,两个整数的除法仍然是整数
print(5//2)
# 打印出来的值是2
# 一种算法%  余数运算 可以得到两个整数相除的余数
print(10%3)
# 打印出来的值是1

# Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）

# 字符串
# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言

