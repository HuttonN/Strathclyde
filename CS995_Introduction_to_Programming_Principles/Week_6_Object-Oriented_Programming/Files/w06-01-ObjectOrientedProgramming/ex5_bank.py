class Account:
    """
    A class to represent a bank account, including a
    list of transactions.
    """
    def __init__(self):
        self.transactions = []

    def income(self):
        """
        A function to return the total income, which comprises
        the sum of the positive transactions.
        """
        total = 0.
        for value in self.transactions:
            if value > 0:
                total += value
        return total

    def expenditure(self):
        """
        A function to return the total expenditure, which comprises
        the sum of the negative transactions.
        """
        total = 0.
        for value in self.transactions:
            if value < 0:
                total += value
        return total

    def balance(self):
        """
        A function to return the balance of the account, by summing all
        transactions.
        """
        return sum(self.transactions)


"""
A program to create an account, add some transactions
and get the properties of the account.
"""
account = Account()
account.transactions.append(1.)
account.transactions.append(-0.5)
print(account.balance())
print(account.expenditure())
print(account.income())
