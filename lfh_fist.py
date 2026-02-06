
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


