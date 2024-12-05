from datetime import datetime
import unittest
from file_catalogue import File, Directory


class TestFile(unittest.TestCase):
    def test_repr(self):
        time_now = datetime.now()
        file = File("my.txt",
                    10,
                    True,
                    "Hi there",
                    time_now.isoformat())
        new_file = eval(str(file))
        self.assertEqual(file, new_file)


class TestDirectory(unittest.TestCase):
    def test_repr(self):
        time_now = datetime.now()
        test_dir = Directory("user", files=[
            File("my.txt",
                 10,
                 True,
                 "Hi there",
                 time_now.isoformat()),
            File("my2.txt",
                 12,
                 False,
                 "Hi there!",
                 time_now.isoformat())
        ])
        new_dir = eval(str(test_dir))
        self.assertEqual(test_dir.name, new_dir.name)
        self.assertEqual(test_dir.files, new_dir.files)

    def test_csv_io(self):
        time_now = datetime.now()
        test_dir = Directory("user", files=[
            File("my.txt",
                 10,
                 True,
                 "Hi there",
                 time_now.isoformat()),
            File("my2.txt",
                 12,
                 False,
                 "Hi there!",
                 time_now.isoformat())
        ])
        test_dir.to_csv("test_output.csv")
        new_dir = Directory("user")
        new_dir.from_csv("test_output.csv")
        self.assertEqual(test_dir.files, new_dir.files)


if __name__ == "__main__":
    unittest.main()
