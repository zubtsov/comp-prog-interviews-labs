# https://edube.org/learn/python-advanced-1/lab-2

class AccountException(Exception):
    pass


class BankAccount(object):
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, _):
        raise AccountException('You can\'t change the account number')

    @account_number.deleter
    def account_number(self):
        if self.__balance != 0:
            raise AccountException('You can\'t delete an account with non-zero balance')
        print('Deleting account number')
        del self.__account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise AccountException('The balance can\'t be negative')
        if abs(self.__balance - new_balance) >= 100000:
            print('Warning: a large amount of money is being deposited or withdrawn')
        self.__balance = new_balance


if __name__ == '__main__':
    ba = BankAccount(123)
    print(ba.account_number)
    print(ba.balance)

    ba.balance = 1000
    try:
        ba.balance = -200
    except AccountException as ae:
        print(ae)
    try:
        ba.account_number = 321
    except AccountException as ae:
        print(ae)
    ba.balance = 1000000
    try:
        del ba.account_number
    except AccountException as ae:
        print(ae)
    ba.balance = 0
    del ba.account_number

    try:
        print(ba.account_number)
    except AttributeError as ae:
        print(ae)
    print(ba.balance)
