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


class Admin(User):
    def __init__(self,first_name,last_name,age,sex,address):
        super().__init__(first_name,last_name,age,sex,address)
        self.privileges = Privileges(['can add post', 'can delete post', 'can ban user'],first_name)

    def show_privileges(self):
        self.privileges.show_privileges()


class Privileges:
    def __init__(self, privileges, first_name):
        self.privileges = privileges
        self.first_name = first_name

    def show_privileges(self):
        if len(self.privileges) == 0:
            print('该用户没有权限')
            return
        auth_str = ''
        for item in self.privileges:
            auth_str += item + ' '
            print(f'{self.first_name}的权限有{auth_str}')
