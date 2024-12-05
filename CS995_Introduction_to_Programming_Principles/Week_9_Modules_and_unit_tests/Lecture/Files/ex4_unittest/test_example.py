import example
import unittest


class TestExample(unittest.TestCase):
    """
    A test case to test the example module.
    """
    def test_double(self):
        """
        A function to test the double function.
        """
        self.assertEqual(example.double(2), 4)


if __name__ == "__main__":
    unittest.main()
