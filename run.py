#!/usr/bin/env python3.9
from random import randint
import random

from user import User
from credentials import Credentials


#User section

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save user 
    '''
    user.save_user()
    
def delete_user(username): 
    '''
    Function delete user
    '''
    User.delete_user(username) 
    
def  check_user(username): 
    """
    Function to check if user exists
    """
    return User.check_user(username)
    
def check_user_exist(username, password):
    """
    function that checks the username and confirms the password
    """
    return User.check_user_exists(username, password)


#Credentials section

def create_credentials(account,username,password):
    '''
    Function to create a new credentials
    '''
    new_credentials = Credentials(account,username,password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials 
    '''
    Credentials.save_credentials(credentials)
    
def delete_credentials(account) :
    """
    Function to delete account credentials
    """ 
    return Credentials.delete_credentials(account)

def find_by_acc(account):
    """
    Function to search for an account
    """
    return Credentials.find_by_acc(account)

def display_credentials():
    """
    Funtion to display credentials
    """
    return Credentials.display_credentials()

# def random_password(passwordLength):  
#     """
#     Function to generate a random password for the user
#     """
#     return Credentials.generate_password(passwordLength)


def main():
    print("Hello,Welcome to My Password Locker.What is your name?") 
    user_name = input()
    print(f'Hey {user_name}. what would you like to do?') 
    print('\n')
    while True:
                    print("Use these short codes : ca - create account,log -login,  ex -exit  ")
                    short_code = input().lower()

                    if short_code == 'ca':
                            print("User")
                            print("-"*20)

                            print ("Username:")
                            username = input()
                            
                            print ("Password:")
                            password = input()
                            
                            save_user(create_user(username,password))
                            print('*'*20)
                            print(
                                f"Hello {user_name} Your account has been created successfully. Kindly login to access your account")
                            print('*'*20)

                    elif short_code == "log":
                            print("Welcome!")
                            print ("Username:")
                            username = input()
                            print ("Password:")
                            password = input()
                            if  check_user_exist(username, password):
                                print("Logged in successfully") 
                                while True:
                                    print("Use the following short codes to check your credentials:cc -create credentials,sc- store credentials,dip- display credentials,ex- exit")
                                    short_code = input().lower()
                                    if short_code == "sc":
                                        print ("Account:")
                                        account = input()
                                        print("Username:")
                                        username = input()
                                        print ("Password:")
                                        password = input()
                                        
                                        save_credentials(create_credentials(account,username,password))
                                        print(f"Your {account} details have been saved.")
                                        print("-"*20)
                                       
                    
                                    elif short_code == "dip":
                                        if display_credentials():
                                           print("Below is a list of your credentials:")
                                           for display in display_credentials():
                                            print(f"Account:{display.account} \n Username:{display.username} \n Password:{display.password}")
                                        else:
                                            print("Your credentials are not available")
                                            print("-"*20)
                                            
                                    elif short_code =="cc":
                                        print("User")
                                        print("-"*20)

                                        print ("Username:")
                                        username = input()
                                        
                                        print ("Account:")
                                        account = input()
                                        while True:
                                            print("Would you like to cp- create password, allow us to generate a password for you,rp-random password")
                                            random = input().lower()
                                            if random =="cp":
                                                print("Create your password")
                                                password =input()
                                            elif random =="rp":
                                                print("What length of password do you want?")
                                                length=int(input())
                                                set ="1qaz2wsx3edc4rfv5tgbyhn7ujm!#$^&AQL9D6GHMPX"
                                                password=""
                                                for y in range(length):
                                                    y=chr(randint(65,90)).lower()
                                                    # newpass=str(password) + y
                                                    password=password+y
                                                print(f"Password has been generated successfully. Your password is {password}")
                                                
                                            break        
                                                 
                                    save_credentials(create_credentials(account,username,password))
                                    print('*'*20)
                            elif short_code == "ex":
                                print ("Thank you for reaching out to My Password Locker!Bye...")
                                break
                            else:
                                print("Kindly use the shortcodes provided.")
                    else:
                        print("Invalid short codes.Try again!")
  
                            
                    
                                    
                                    
                    
                                    
                            
                                     
                                    
                                      
                                        
                                        
                                        
                                        
                            
                            
                                        
                                        
                           
                            
                                               
                          
                               
                           
                        
                       
                        
                                        
                                            

if __name__ == '__main__':
     main()                            