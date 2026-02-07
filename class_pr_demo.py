from random import randint,choice
from class_pr import Die

my_die = Die(6)
my_die.roll_die()
ten_die = Die(10)
my_die.roll_die()
twenty_die = Die(20)
my_die.roll_die()

my_tuple = (18,2,35,40,58,62,71,86,9,37,'u','p','c','e','l')
random_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count = 0
is_continue = True
while is_continue:
    my_ans = randint(0, 1000)
    if my_ans in my_tuple:
        count += 1
        print(f'恭喜您，中奖了，中奖号码为{my_ans},当前共抽取了{count}次，中奖概率为{count/1000 * 100}%')
        is_continue = False
    else:
        count+=1

