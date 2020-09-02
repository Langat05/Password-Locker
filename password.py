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