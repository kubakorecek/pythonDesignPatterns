"""
Factory it is defining interface and delay initialisation until Runtime.

we use classical example of Bank account. We are going to use setters and getters to protect the attributes.
"""

class Bank(object):
    """
        Parent, or so Called Interface CLASS which is like a blue print.

    """
    
    def __init__(self, balance = 1000):
        self._balance = balance
        self.acc_number =

    def withdrawal(self): pass

    def addmoney(self): pass

    def transfermoney(self):pass

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        print(amount.__class__.__name__)
        if amount.__class__.__name__ == 'int' or amount.__class__.__name__ == 'float':

            self._balance = amount
        else:
            assert 0, "Wrong type"

class SavingBankAccount(Bank):
    """
        Saving bank account.

    """

    def __init__(self):
        super(SavingBankAccount, self).__init__()

    def withdrawal(self, amout):
        self.balance -= amout

    def addmoney(self, amount):
        self.balance += amount

    def transfermoney(self):
        pass

if __name__ == '__main__':
    #a = SavingBankAccount()
    #a.balance
    #a.balance = 500
    pass
