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
