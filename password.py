class User:
    user_list = []
    def __init__(self,name,username,password):
        self.name = name
        self.username = username
        self.password = password

    def save_user(self):
        User.user_list.append(self)    

    def delete_user(self):
        User.user_list.remove(self)    

    @classmethod
    def find_user_by_name(cls,name):
        for user in cls.user_list:
            if user.name == name:
                return user

