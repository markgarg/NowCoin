from functions import isValidTxn

def main():
    state = {u'Alice':5,u'Bob':5}

    print(isValidTxn({u'Alice': -3, u'Bob': 3},state))  # Basic transaction- this works great!
    print(isValidTxn({u'Alice': -4, u'Bob': 3},state))  # But we can't create or destroy tokens!
    print(isValidTxn({u'Alice': -6, u'Bob': 6},state))  # We also can't overdraft our account.
    print(isValidTxn({u'Alice': -4, u'Bob': 2,'Lisa':2},state)) # Creating new users is valid
    print(isValidTxn({u'Alice': -4, u'Bob': 3,'Lisa':2},state)) # But the same rules still apply!

if __name__ == '__main__':
    main()