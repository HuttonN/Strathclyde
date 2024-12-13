class Purchase:  
    """
    A class to hold information concerning one
    purchase.
    """

    def __init__(self, item_id, amount_paid):
        self.item_id = item_id
        self.amount_paid = amount_paid

    def __repr__(self):
        s = "Purchase("
        s += f"item_id={self.item_id},"
        s += f"amount_paid={self.amount_paid})"
        return s


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

    def __repr__(self):
        s = "Customer("
        s += f"customer_id={self.customer_id},"
        s += f"first_name=\"{self.first_name}\","
        s += f"surname=\"{self.surname}\","
        s += f"purchases={self.purchases})"
        return s

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