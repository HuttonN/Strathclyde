import csv
import os


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


def check_columns(file_name, expected_columns, row_dict):
    """
    Check all column names are present.  If a column is
    missing, the function returns True.
    """
    data_error = False
    for expected_column in expected_columns:
        if expected_column not in row_dict.keys():
            data_error = True
            msg = "Error: cannot find the column"
            msg += f" {expected_column} in the input"
            msg += f" data file {file_name}."
            print(msg)
    return data_error


def load_customers(customers, file_name):
    """
    A function create Customer objects from an input CSV file.
    """

    customers.clear()
    input_file = open(file_name, "r", newline='')
    dict_reader = csv.DictReader(input_file)

    # These columns should be found in the CSV input file.
    expected_columns = [
        "id",
        "first_name",
        "surname"
    ]

    # Read the CSV file.
    for row_dict in dict_reader:
        data_error = check_columns(file_name, expected_columns, row_dict)
        if data_error:
            break

        # Create the object.
        customer = Customer(int(row_dict["id"]),
                            str(row_dict["first_name"]),
                            str(row_dict["surname"]))

        # Store the object for matching.
        customers[customer.customer_id] = customer

    input_file.close()


def load_purchases(customers, file_name):
    """
    A function create Purchase objects from an input CSV file.
    The function matches the Purchase objects with the Customers
    that are given in the customers input dictionary.
    """

    input_file = open(file_name, "r", newline='')
    dict_reader = csv.DictReader(input_file)

    # These columns should be found in the CSV input file.
    expected_columns = [
        "customer_id",
        "item_id",
        "amount_paid"
    ]

    # Read the CSV file.
    for row_dict in dict_reader:
        data_error = check_columns(file_name, expected_columns, row_dict)
        if data_error:
            break

        # Create the object.
        purchase = Purchase(int(row_dict["item_id"]),
                            float(row_dict["amount_paid"]))

        customer_id = int(row_dict["customer_id"])

        # Check if the customer_id is found.
        if customer_id not in customers.keys():
            msg = "Error: cannot find customer_id"
            msg += f" {customer_id} when reading purchase item_id"
            msg += f" {purchase.item_id}."
            print(msg)
            continue

        customers[customer_id].purchases.append(purchase)

    input_file.close()


def load_data():
    """
    A function to create Purchases and Customer objects from input
    CSV data files.  The function expects that the data files are
    in the present working directory.
    """

    # Make sure that the files are available.
    files = ["purchases.csv", "customers.csv"]
    for file in files:

        # If one of the files is missing.
        if not os.path.isfile(file):
            print("Error: cannot find the {file} file.")
            return {}

    customers = {}
    load_customers(customers, "customers.csv")
    load_purchases(customers, "purchases.csv")
    return customers


if __name__ == '__main__':
    """
    A test program.
    """
    customers = load_data()
    print(customers)
