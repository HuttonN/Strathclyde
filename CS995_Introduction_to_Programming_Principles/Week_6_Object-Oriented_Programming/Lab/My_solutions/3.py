"""Create two classes named Customer and Purchase.
• The classes should be designed to contain the contents of Table 1 and 2. The Customer class should
include a list data member to hold Purchase objects.
Table 1: Customers
id  first_name  surname
1   Amiee   Greene
2   Maia    Morley
3   Charleigh   Cano
4   Franklin    Torres
5   Mitchell    Page
6   Momina  Thornton
7   Cheryl  Devlin
8   Isobel  Orozco
9   Nicolas Adams
10  Devante Rodriguez

Table 2: Purchases, where the foreign key customer_id relates to the id value in the Customers table.
customer_id item_id amount_paid
3   1   100
2   3   123
6   5   40
1   2   23
3   1   100
5   5   40
7   15  46
2   7   3.02
1   10  22
8   12  45.95
4   17  33
4   17  33
2   5   40

• Add a member function to the Customer class to return a table of item_id and amount_paid. The
return value should be a formatted string that includes the values and description of what they are.
The string should use a tab (\t) character to separate the two columns.
• Add a member function to the Customer class to return a total amount_paid by a specific customer.
The function should loop over all Purchase objects and return a floating point number.
"""

class Purchase:
    """
    A class to hold information concerning an individual purchase
    """

    def __init__(self, item_id, amount_paid):
        self.item_id = item_id
        self.amount_paid = amount_paid

class Customer:
    """
    A class to hold customer details and their associated purchases
    """

    def __init__(self, customer_id, first_name, surname, purchases = []):
        self.customer_id = customer_id
        self.first_name = first_name
        self.surname = surname
        self.purchases = purchases.copy()

    def purchases_summary(self):
        """
        A function to return the purchases summary string for a customer.
        """

        s = "customer_id: " + str(self.customer_id) + "\n"
        s += "item_id" + "\t" + "amount_paid"
        for purchase in self.purchases:
            s += "\n"
            s += str(purchase.item_id) + "\t" + str(purchase.amount_paid)
        return s
    
    def total_paid(self):
        """
        A function to return the total amount paid by a customer
        """

        total = 0
        for purchase in self.purchases:
            total += purchase.amount_paid
        return total