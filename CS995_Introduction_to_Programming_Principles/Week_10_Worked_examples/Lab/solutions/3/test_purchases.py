import unittest
import purchases


class TestPurchases(unittest.TestCase):
    def test_total_paid(self):
        customer = purchases.Customer(1, "Joe", "Bloggs")
        customer.purchases.append(purchases.Purchase(1, 20.))
        customer.purchases.append(purchases.Purchase(2, 30.))
        self.assertEqual(customer.total_paid(), 50.)

    def test_purchases_summary(self):
        customer_id = 1
        item_id = 1
        amount_paid = 20.
        customer = purchases.Customer(customer_id, "Joe", "Bloggs")
        purchase = purchases.Purchase(item_id, amount_paid)
        customer.purchases.append(purchase)

        # Build the expected string.
        expected_string = f"customer_id:{customer_id}\n"
        expected_string += "item_id" + "\t" + "amount_paid\n"
        expected_string += f"{purchase.item_id}\t{purchase.amount_paid}"

        self.assertEqual(customer.purchases_summary(), expected_string)

    def test_load_data(self):
        customers = purchases.load_data()
        self.assertIn(1, customers.keys())
        customer = customers[1]
        self.assertEqual(customer.first_name, "Amiee")
        self.assertEqual(customer.surname, "Greene")
        self.assertEqual(len(customer.purchases), 2)


if __name__ == '__main__':
    unittest.main()
