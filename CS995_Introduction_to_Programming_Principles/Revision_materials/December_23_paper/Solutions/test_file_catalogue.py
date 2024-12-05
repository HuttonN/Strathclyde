import unittest
from datetime import datetime
from file_catalogue import File
from file_catalogue import Directory

class TestFileCatalogue(unittest.TestCase):
    def test_file_repr(self):
        file = File(name="test.txt", size=100, executable=False, content="Hello", modified="2023-12-01T12:00:00")
        self.assertEqual(eval(repr(file)), file)
    
    def test_directory_repr(self):
        file = File(name="test.txt", size=100, executable=False, content="Hello", modified="2023-12-01T12:00:00")
        directory = Directory(name="my_directory", files=[file])
        self.assertEqual(eval(repr(directory)), directory)
    
    def test_to_csv_and_from_csv(self):
        file = File(name="test.txt", size=100, executable=False, content="Hello", modified="2023-12-01T12:00:00")
        directory = Directory(name="my_directory", files=[file])
        directory.to_csv("test.csv")
        new_directory = Directory(name="new_directory")
        new_directory.from_csv("test.csv")
        self.assertEqual(directory.files, new_directory.files)
    
    def test_find_by_name(self):
        file1 = File(name="test1.txt", size=100)
        file2 = File(name="test2.txt", size=200)
        directory = Directory(name="my_directory", files=[file1, file2])
        self.assertEqual(directory.find_by_name(r"test1.*"), [file1])
    
    def test_find_by_modified(self):
        file1 = File(name="test1.txt", size=100, modified="2023-12-01T12:00:00")
        file2 = File(name="test2.txt", size=200, modified="2023-12-02T12:00:00")
        directory = Directory(name="my_directory", files=[file1, file2])
        self.assertEqual(directory.find_by_modified(datetime(2023, 12, 2)), [file1, file2])
        self.assertEqual(directory.find_by_modified(datetime(2023, 12, 2), comparison=1), [file2])
