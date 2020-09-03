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
        '''
        Method that takes in a name and returns a user that matches that name.

        Args:
            name:  name to search for
        Returns :
            User that matches the name.
        '''
        for user in cls.user_list:
            if user.name == name:
                return user


    @classmethod
    def user_exist(cls,name):
        '''
        Method that checks if a user exists from the user list.
        Args:
            name: name to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.name == name:
                    return True

        return False   