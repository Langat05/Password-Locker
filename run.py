from password import User , Credential
import random
import getpass
import string
import uuid


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

def find_credential(username):
    '''
    Function that finds a credential by username and returns the credential
    '''
    return Credential.find_by_username(username)    

def check_existing_credentials(username):
    '''
    Function that check if a credential exists with that username and return a Boolean
    '''
    return Credential.credential_exist(username)      

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()  

def main():
    print("What is your name?")
    name = input()

    ask = input(f"{name} Do you have an account? yes or no > ")

    if ask == "no":
        print("Signup now")
        username = input(f"{username}. Do you want the system to generate password for you? yes or no > ")
        if create == "no":
            print("create your password then")
            getpass.getpass()
            print("Sign in successfull")

        while True:
            print("""
            Use the short codes: cc to create new credential
                                 dc to display credentials
                                 fc to find credential
                                 dl to delete credential
                                 rp to generate random password
                                 ex to exit
                                 """)

            short_code == input ("Navicate now using the short codes > ")
            if short_code == "cc": 
                print("Create new account")
                print("-"*12)  

                print("Enter your name(s)")
                name = input("> ")

                print("Enter account for example instagram, facebook or twitter....")
                account = input("> ")

                print("Enter your preffered username")
                username = input("> ")

                print("Enter password")
                password = ("> ")

                save_credential(create_credential(name, account, username, password))

                print("\n")
                print(f"New credential Nam:{name}, account:{account}, and password:{password} have been created")
                print("\n")

            elif short_code == "rp":
                print("Please enter the account you wantto generate password for > ")
                account = input("Enter accounttype > ")




                                
               