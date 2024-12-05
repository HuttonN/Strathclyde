import my_module
import unittest


class TestMyModule(unittest.TestCase):
    def test_swap(self):
        """
        A function to test the swap function.
        """

        # Normal use.
        numbers = [1, 2]
        my_module.swap(numbers)
        self.assertEqual(numbers, [2, 1])

        # With no elements.
        self.assertRaises(IndexError, my_module.swap, [])

        # With an int, rather than a list.
        self.assertRaises(TypeError, my_module.swap, 1)


if __name__ == "__main__":
    unittest.main()
