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

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()     

def create_credential(name, account, username, password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(name,account,username,password)
    return new_credential       

def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()   

def delete_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()
