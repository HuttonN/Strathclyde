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
    def __init__(self, customer_id, item_id, amount_paid):
        self.customer_id = customer_id
        self.item_id = item_id
        self.amount_paid = amount_paid

class Customer:
    def __init__(self, id, first_name, surname):
        self.id = id
        self.first_name = first_name
        self.surname = surname
        self.purchases = []

    def add_purchase(self,purchase):
        self.purchases.append(purchase)

    def get_purchase_table(self):
        table = "Item ID\tAmount Paid"
        for purchase in self.purchases:
            table += f"\n{purchase.item_id}\t{purchase.amount_paid}"
        return table
    
    def total_amount_paid(self):
        total = 0
        for purchase in self.purchases:
            total += purchase.amount_paid
        return total