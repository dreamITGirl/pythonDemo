message=123
print(message)

simple_message = 'hello world'
print(simple_message)
print(type(simple_message))
simple_message = 1234
print(simple_message)

first_name = 'ada'
last_name = 'lovelace'
print(first_name)
print(last_name)
#javascript中一般使用模板字符串进行拼接
full_name = f'{first_name} {last_name}'
print(full_name)
#在js中首字母大写需要额外使用js方法进行实现
print(full_name.title()) #Ada Lovelace
print(full_name.upper())
print(full_name.lower())



#添加空白
simple_exam1 = 'python'
print(simple_exam1)
# \t标识缩进符
simple_exam2= '\tpython'
print(simple_exam2)
print('python\nis a\nsimple\nlanguages')
#删除字符串中的空白，在javascript中，可以通过trim()来实现删除字符串两端的空白
favorite = ' banana'
print(favorite)
favorite_fruits = 'banana'
print(favorite_fruits)
# 删除左侧空格 lstrip()
# 删除右侧空格 rstrip()
# 同时删除字符串两端的空格 strip()
print(favorite.lstrip())


name = 'eric'
info = 'would you like to learn some Python today'
# Hello Eric,would you like to learn some Python today?
print(f'Hello {name.title()},{info}?')
print(len(name)) # 4

famous_message = 'A person who never made a mistake never tried anything new.'
famous_person = 'albert einstein'
# Albert Einstein once said 'A person who never made a mistake never tried anything new.'
print(f"{famous_person.title()} once said '{famous_message}'")


print('''line1\n line2\n\tline3''')

print('''line2
... line3
... line4
''')

name = input('please enter your name: ')
print('hello',name)



