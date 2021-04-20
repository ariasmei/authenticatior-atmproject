import random
from datetime import datetime
import validation

from validation import accountnumvalidation

import database
from getpass import getpass


def accountgenerator():
    return random.randrange(1111111111, 9999999999)


def initial():
    validoptionselected = False
    print("welcome to Bank of America ")
    now = datetime.now()
    print("Todays date and time is .... ", now)

    while not validoptionselected:
        have_account = int(input("do you have an account with us  1= yes . 2 = no?"))
        if have_account == 1:
            validoptionselected = True
            login()
        elif have_account == 2:
            validoptionselected = True
            print(register())

        else:
            print("you have selected an invalid iption")
            initial()


# def login():
# print("welcome again, log in")
# accountnumfromuser = int(input("what is you accout number")
# password = input("what is your password")
# if account_number_validation(accountnumfromuser):
# user = database.authenticated_user(account_number_from_user, password)
# if user:
# bankoperations(user)

##print("invalid account ot password")
# login()
def login():
    print("********* Login ***********")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")
    account_number_from_user = input("What is your account number? \n")

    for accountNumber, userDetails in database.items():
        if (accountNumber == accountNumberFromUser):
            if (userDetails[3] == password):
                bankOperation(userDetails)

    print('Invalid account or password')
    login()

    is_valid_account_number = validation.account_number_validation(account_number_from_user)





def register():
    print("since you are not an account holder at Bank of America well have to register you")
    email = input("what is your email address")
    first_name = input("what us your first name")
    last_name = input("what us your last name")
    password = input("Create a unique password for yourself")
    accnumber = accountgenerator()

    try:
        accnumber = accountgenerator()
    except ValueError:
        print("account generation due to unknown reason")
        exit()

        # database[accnumber] = [first_name, last_name, email, password]
    is_user_created = database.create(accnumber, first_name, last_name, email, password, 0)

    if is_user_created:

        print("your account has been created ")
        print("your accoumt number is.....")
        print(accnumber)
        login()
    else:
        print('something went wrong try again')


def bankoperations(user):
    print("Welcome   %s %s " % (user[0], user[1]))

    selectedption = int(input("what would you like to do ? (1) withdraw, (2) deposit, (3) logout, (4) complain"))
    if selectedption == 1:
        withdrawloperation()

    elif selectedption == 2:

        depositoperation()
    elif selectedption == 3:

        logout()
    elif selectedption == 4:
        complain()

        exit()
    else:
        print("invalid option selected ")
        bankoperations(user)


def withdrawloperation():
    withdrawamount = int(input("how much would you like to withdraw "))
    print(withdrawamount)
    if withdrawamount == int or float:
        print("your withdrawl is complete thank you ")


def depositoperation():
    depositamount = int(input("how much would you like to deposit "))
    print(depositamount)
    if depositamount == int or float:
        print("your deposit is complete thank you ")


def logout():
    print("you have been logged out and taken back to the main menu")
    login()


def complain():
    usercomplaint = input("what issue would you like to report ")
    if usercomplaint == str:
        print("Were sorry to hear that call 1800-234-5678 to get in touch with a repesentitive ")


def accountnumvalidation(account_num):
    if account_num:

        if len(str(account_num)) == 10:

            try:
                int(account_num)
            except ValueError:
                print("invalid account number, account number should be an integer")
                return False
            except TypeError:
                print("invalid accoutn type")
                return False
        else:
            print("account number can be more than 10 digits ")

    else:
        print("account number not found")
        return False


initial()
