'''
This Python exam will involve implementing a bank program that manages bank accounts and
allows for deposits, withdrawals, and purchases.
'''

def init_bank_accounts(accounts, deposits, withdrawals):
    '''
    Loads the given 3 files, stores the information for individual bank accounts in a dictionary,
    and calculates the account balance.

    Accounts file contains information about bank accounts.
    Each row contains an account number, a first name, and a last name, separated by vertical pipe (|).
    Example:
    1|Brandon|Krakowsky

    Deposits file contains a list of deposits for a given account number.
    Each row contains an account number, and a list of deposit amounts, separated by a comma (,).
    Example:
    1,234.5,6352.89,1,97.60

    Withdrawals file contains a list of withdrawals for a given account number.
    Each row contains an account number, and a list of withdrawal amounts, separated by a comma (,).
    Example:
    1,56.3,72.1

    Stores all of the account information in a dictionary named 'bank_accounts', where the account number is the key,
    and the value is a nested dictionary.  The keys in the nested dictionary are first_name, last_name, and balance,
    with the corresponding values.
    Example:
    {'1': {'first_name': 'Brandon', 'last_name': 'Krakowsky', 'balance': 6557.59}}

    This function calculates the total balance for each account by taking the total deposit amount
    and subtracting the total withdrawal amount.
    '''

    bank_accounts = {}

    #insert code

    return bank_accounts

def round_balance(bank_accounts, account_number):
    '''Rounds the given account balance.'''

    pass

def get_account_info(bank_accounts, account_number):
    '''Returns the account information for the given account_number as a dictionary.
    Example:
    {'first_name': 'Brandon', 'last_name': 'Krakowsky', 'balance': 6557.59}
    If the account doesn't exist, returns None.
    '''

    pass

def withdraw(bank_accounts, account_number, amount):
    '''Withdraws the given amount from the account with the given account_number.
    Raises a RuntimeError if the given amount is greater than the available balance.
    If the account doesn't exist, prints a friendly message.
    Rounds and prints the new balance.
    '''

    pass

def deposit(bank_accounts, account_number, amount):
    '''Deposits the given amount into the account with the given account_number.
    If the account doesn't exist, prints a friendly message.
    Rounds and prints the new balance.
    '''

    pass

def purchase(bank_accounts, account_number, amounts):
    '''Makes a purchase with the total of the given amounts from the account with the given account_number.
    Raises a RuntimeError if the total purchase, plus the sales tax (6%), is greater than the available balance.
    If the account doesn't exist, prints a friendly message.
    Rounds and prints the new balance.
    '''

    pass

def calculate_sales_tax(amount):
    '''Calculates and returns a 6% sales tax for the given amount.'''

    pass

def main():

    #load and get all account info
    bank_accounts = init_bank_accounts('accounts.txt', 'deposits.csv', 'withdrawals.csv')

    #for testing
    #print(bank_accounts)

    while True:

        #print welcome and options
        print('\nWelcome to the bank!  What would you like to do?')
        print('1: Get account info')
        print('2: Make a deposit')
        print('3: Make a withdrawal')
        print('4: Make a purchase')
        print('0: Leave the bank')

        # get user input
        option_input = input('\n')

        # try to cast to int
        try:
            option = int(option_input)

        # catch ValueError
        except ValueError:
            print("Invalid option.")

        else:

            #check options
            if (option == 1):

                #get account number and print account info
                account_number = input('Account number? ')
                print(get_account_info(bank_accounts, account_number))

            elif (option == 2):

                # get account number and amount and make deposit
                account_number = input('Account number? ')

                # input cast to float
                amount = float(input('Amount? '))

                deposit(bank_accounts, account_number, amount)

            elif (option == 3):

                # get account number and amount and make withdrawal
                account_number = input('Account number? ')

                #input cast to float
                amount = float(input('Amount?  '))

                withdraw(bank_accounts, account_number, amount)

            elif (option == 4):

                # get account number and amounts and make purchase
                account_number = input('Account number? ')
                amounts = input('Amounts (as comma separated list)? ')

                # convert given amounts to list
                amount_list = amounts.split(',')
                amount_list = [float(i) for i in amount_list]

                purchase(bank_accounts, account_number, amount_list)

            elif (option == 0):

                # print message and leave the bank
                print('Goodbye!')
                break


if __name__ == "__main__":
    main()
