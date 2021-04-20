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
