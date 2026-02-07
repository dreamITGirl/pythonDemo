from restaurant import Restaurant
from user import Admin

my_restaurant = Restaurant('小牛牛','西式快餐')
my_restaurant.describe_restaurant()

my_user = Admin('小王','王',18,'男','上海')
my_user.show_privileges()