#for循环
trip_list = ['yunnan','guangxi','fujian','guangzhou','haerbin','xinjiang']
for item in trip_list:
    print(f'I want to travel {item}')
print('But i really lazy,i don`t know where i can go')

animal_list = ['cat',
               'dog',
                'bird' ]
for item in animal_list:
    print(f'I like {item}')
print('But i really lazy,i don`t know where i can go')


#range()
for item in range(1,2):
    print(item)
num_list = list(range(1,11))
print(num_list)
even_list = list(range(2,11,2))
print(even_list) #[2, 4, 6, 8, 10]
odd_list = list(range(1,11,2))
print(odd_list)

digit_list = [1,2,3,4,5,6,7,8,9]
print(min(digit_list))
print(max(digit_list))
print(sum(digit_list))


price_list = list(range(1,21))
print(price_list)
odd_price_list = list(range(1,21,2))
print(odd_price_list)

more_list = list(range(1,100_0000))
# for item in more_list:
#     print(item)

sum_num = sum(more_list)
print(sum_num)

# trip_list = list(range(1,11))
# for item in trip_list:
#     print(item ** 3)
tri_list = [value **3 for value in range(1,11)]
print(tri_list)

#  切片
trip_list = ['yunnan','guangxi','fujian','guangzhou','haerbin','xinjiang']
# print(trip_list[1:4])
# print(trip_list[:4])
# print(trip_list[2:])
# print(trip_list[-3:])
# print(trip_list[1:4:4])
for item in trip_list[2:5]:
    print(f'I want to travel {item}')

list_d = trip_list[:]
print(list_d)
list_d.append('xiamen')
print(list_d)
print(trip_list)
