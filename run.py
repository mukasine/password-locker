#!/usr/bin/env python3.6
from user import User
import string
import random
def create_user(fname,lname,phone,email):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,phone,email)
    return new_user
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

def find_user(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_number(number)
def check_existing_users(number):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(number)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()
def del_user(users):
    '''
    Function to delete a credential
    '''
    users.delete_user()

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))


def main():
    print("Hello Welcome to your user list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    while True:
                    print("Use these short codes : cc - create a new user, dc - display users, fc -find a user, ex -exit the user list , dd- delete user ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New User")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()

                            print("Password ...")
                            print("pg - generate password , ep- Enter password")
                            short_code1=input().lower()
                            if short_code1=='pg':
                                password=pw_gen()
                            elif short_code1=='ep':
                                print("Enter password")
                                password=input()

                            else:
                                print("Please use provided short codes")


                            save_users(create_user(f_name,l_name,p_number,e_address)) # create and save new user.
                            print ('\n')
                            print(f"New User {f_name} {l_name} created")
                        #     print(f"Your new password is {password}")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_users():
                                    print("Here is a list of all your users")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any users saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_users(search_number):
                                    search_user= find_user(search_number)
                                    print(f"{search_user.first_name} {search_user.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_user.phone_number}")
                                    print(f"Email address.......{search_user.email}")
                            else:
                                    print("That user does not exist")

                    elif short_code == 'dd':
                        
                            print("Search for number to delete")

                            search_name = input()

                            if check_existing_users(search_name):
                                search_credential = find_user(search_name)
                                # print(f"ACCOUNT NAME: {search_credential.acc_name} \n PASSWORD: {search_credential.acc_password}")
                                # print("Delete? y(for yes)/n(for no)")
                                # proceed = input().lower()
                                # if proceed == 'y':
                                del_user(search_credential)
                                print("User deleted")
                                #     print("Account deleted")
                                #     break
                                # elif proceed == 'n':
                                #     continue

                            else:
                                print("Contact Does not exist")
                                break              

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
                                 main()
