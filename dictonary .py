import random
from datetime import datetime


def accountgenerator():
    return random.randrange(1111111111, 9999999999)


database = {}


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


def login():
    print("log in")

    accountnumfromuser = int(input("what is you accout number"))
    password = input("what is your password")

    for accountnum, userdetails in database.items():
        if accountnum == accountnumfromuser:
            if userdetails[3] == password:
                bankoperations(userdetails)

    print("invalid account ot password")
    login()


def register():
    print("since you are not an account holder at Bank of America well have to register you")
    email = input("what is your email address")
    first_name = input("what us your first name")
    last_name = input("what us your last name")
    password = input("Create a unique password for yourself")
    accnumber = accountgenerator()
    database[accnumber] = [first_name, last_name, email, password]
    print("your account has been created ")
    print("your accoumt number is.....")
    print(accnumber)
    login()


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


initial()
