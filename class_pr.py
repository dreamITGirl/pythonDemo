# 练习demo
import random
class Die:
    def __init__(self,num_sides=6):
        self.num_sides = num_sides
        self.sides = 10

    def roll_die(self):
        sides_arr = []
        count = self.sides
        while count>0:
            num_si = random.randint(1, self.num_sides)
            sides_arr.append(num_si)
            count-=1
        print(sides_arr)










