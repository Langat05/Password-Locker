from password import User , Credential
import random


def creat_user(name,username,password):
    '''
    Function to create a new user
    '''
    new_user = User(name,username,password)
    return new_user

def generate_password(user):
    """
    Function to generate random password for user
    """
    return user.generate_random_password()      

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()     