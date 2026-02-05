#元组
name  = 'alice'
tuple_list = ('bob',name,'jack')
print(tuple_list)
name = 'jerry'
tuple_list = ('bob',name,'jack')
print(tuple_list)

tuple_list = ('amy','sum','jerry')
print(tuple_list)

foods_list = ('apple','banana','mango','orig','polo')
print(foods_list)

for food in foods_list:
    print(food)

# foods_list[1] = 'banana' #报错 'tuple' object does not support item assignment
# print(foods_list)
su_list = ('apple','fruit')
print(su_list)
foods_list = su_list + foods_list[3:]
print(foods_list)