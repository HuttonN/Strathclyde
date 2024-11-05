class Purchase:
    """
    A class to hold information concerning one
    purchase.
    """

    def __init__(self, item_id, amount_paid):
        self.item_id = item_id
        self.amount_paid = amount_paid


class Customer:
    """
    A class to hold customer details and their associated
    purchases.
    """

    def __init__(self,
                 customer_id,
                 first_name,
                 surname,
                 purchases=[]):
        self.customer_id = customer_id
        self.first_name = first_name
        self.surname = surname
        self.purchases = purchases.copy()

    def purchases_summary(self):
        """
        A function to return the purchases summary string for a customer.
        """

        s = "customer_id:" + str(self.customer_id) + "\n"
        s += "item_id" + "\t" + "amount_paid"
        for purchase in self.purchases:
            s += "\n"
            s += str(purchase.item_id) + "\t" + str(purchase.amount_paid)
        return s

    def total_paid(self):
        """
        A function to return the total amount paid by a customer.
        """

        total = 0.
        for purchase in self.purchases:
            total += purchase.amount_paid
        return total


"""
A program to demonstrate the Customer and Purchase class.
"""
customer = Customer(1, "Joe", "Bloggs")
customer.purchases.append(Purchase(1, 20.))
customer.purchases.append(Purchase(2, 30.))
print(customer.purchases_summary())
print(customer.total_paid())
