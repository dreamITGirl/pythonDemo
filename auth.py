from user import User
from user import Privileges
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
