class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f'{self.restaurant_name}的菜系是{self.cuisine_type}')
    def open_restaurant(self):
        print(f'{self.restaurant_name}正在营业')
    def set_number_served(self,number_served):
        self.number_served = number_served
    def incrimment_number_served(self,number_served):
        self.number_served += number_served
        print(f'{self.restaurant_name}今天已经服务了{self.number_served}人')

class IceCreamStand():
    def __init__(self,restaurant_name,cuisine_type):
        self.flavors = ['香草味','巧克力','蓝莓']
        self.restaurant = Restaurant(restaurant_name, cuisine_type)
    def show_flavors(self):
        str = ''
        for item in self.flavors:
            str+=item+' '
        print(f'{self.restaurant.restaurant_name}的冰淇淋种类有{str}')
my_icecream_stand = IceCreamStand('小牛牛', '西式快餐')
my_icecream_stand.show_flavors()
# my_restaurant = Restaurant('小牛牛', '西式快餐')
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()
# my_restaurant.set_number_served(0)
# my_restaurant.incrimment_number_served(100)

# jd_restaurant = Restaurant('京东', '西式快餐')
# jd_restaurant.describe_restaurant()
#
# lyr_restaurant = Restaurant('lyr', '西式快餐')
# lyr_restaurant.describe_restaurant()


class User:
    def __init__(self,first_name,last_name,age,sex,address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.address = address
        self.login_attempts = 0
    def describe_user(self):
        print(f'{self.first_name} {self.last_name} {self.age} {self.sex}')
    def greet_user(self):
        print(f'hello {self.first_name}')
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'{self.first_name}登录失败次数为{self.login_attempts}')
    def reset_login_attempts(self):
        self.login_attempts = 0
        print('登录失败次数已重置为0')

# user_one = User('小王','王',18,'男','上海')
# user_one.describe_user()
# user_one.greet_user()
# user_one.increment_login_attempts()
# user_one.increment_login_attempts()
# user_one.increment_login_attempts()
# user_one.reset_login_attempts()

# class Admin(User):
#     def __init__(self,first_name,last_name,age,sex,address):
#         super().__init__(first_name,last_name,age,sex,address)
#         self.privileges = ['can add post','can delete post','can ban user']
#     def show_privileges(self):
#         if len(self.privileges) == 0:
#             print('该用户没有权限')
#             return
#         auth_str = ''
#         for item in self.privileges:
#             auth_str+=item+' '
#             print(f'{self.first_name}的权限有{auth_str}')
#
# user_admin = Admin('小王','王',18,'男','上海')
# user_admin.show_privileges()

class Privileges:
    def __init__(self, privileges,first_name):
        self.privileges = privileges
        self.first_name = first_name
    def show_privileges(self):
        if len(self.privileges) == 0:
            print('该用户没有权限')
            return
        auth_str = ''
        for item in self.privileges:
            auth_str+=item+' '
            print(f'{self.first_name}的权限有{auth_str}')

class Admin(User):
    def __init__(self,first_name,last_name,age,sex,address):
        super().__init__(first_name,last_name,age,sex,address)
        self.privileges = Privileges(['can add post', 'can delete post', 'can ban user'],first_name)
    def show_privileges(self):
        self.privileges.show_privileges()

admin_user = Admin('小王','王',18,'男','上海')
admin_user.show_privileges()

class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')
    def update_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print(f'The battery has been upgraded to {self.battery_size}-kWh.')
        else:
            print('The battery is already upgraded.')
    def get_range(self):
       if self.battery_size == 70:
           range = 240
       elif self.battery_size == 100:
           range = 270
       message = f"This car can go approximately {range}"
       message += " miles on a full charge."
       print(message)

my_buggy = Battery()
my_buggy.get_range()
my_buggy.update_battery()
my_buggy.get_range()