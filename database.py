import validation
import os

user_db_path = 'venv/userdetails/'


def create(account_number, user_details):
    global f
    completion_state = False
    try:
        f = open('venv/userdetails/' + str(account_number) + ".txt", "x")

    except FileExistsError:
        print('user already exist ')
        return completion_state
        delete(account_number)
    else:
        f.write(str(user_details))
        completion_state = True
    finally:
        f.close()
        return completion_state


def update(user_account_number):
    print('update user record')


def read(user_account_number):
    is_valid_account_number = validation.account_number_validation(user_account_number)

    try:

        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path + user_account_number, "r")

    except FileNotFoundError:

        print("User not found")

    except FileExistsError:

        print("User doesn't exist")

    except TypeError:

        print("Invalid account number format")

    else:

        return f.readline()

    return False


def delete(user_account_number):
    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):

        try:

            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:

            print("User not found")

        finally:

            return is_delete_successful


def does_email_exist(email):
    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False


def does_account_number_exist(account_number):
    all_users = os.listdir(user_db_path)

    for user in all_users:

        if user == str(account_number) + ".txt":
            return True

    return False


def authenticated_user(account_number, password):
    if does_account_number_exist(account_number):

        user = str.split(read(account_number), ',')

        if password == user[3]:
            return user

    return False

def authenticated_user(account_number, password):

    if does_account_number_exist(account_number):

        user = str.split(read(account_number), ',')

        if password == user[3]:
            return user

    return False

