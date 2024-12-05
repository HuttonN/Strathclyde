import io
import unittest
from datetime import datetime
from basket_io import BasketItem, list_to_file, file_to_list


class TestBasketItem(unittest.TestCase):
    def test_repr(self):
        time_now = datetime.now()
        item = BasketItem("Ice-cream", 1, time_now.isoformat())
        new_item = eval(str(item))
        self.assertEqual(item.name, new_item.name)
        self.assertEqual(item.quantity, new_item.quantity)


class TestParsing(unittest.TestCase):
    def test_write_read(self):
        text_io = io.StringIO()
        records = [
            [
                BasketItem("Ice-cream",
                           1,
                           datetime(2023, 11, 11).isoformat()),
                BasketItem("Washing up liquid",
                           1,
                           datetime(2023, 11, 11).isoformat())
            ],
            [
                BasketItem("Potato",
                           20,
                           datetime(2023, 11, 12).isoformat()),
            ]
        ]
        list_to_file(text_io, records)
        text_io.seek(0)
        new_records = []
        file_to_list(text_io, new_records)
        self.assertEqual(str(records), str(new_records))


if __name__ == "__main__":
    unittest.main()
