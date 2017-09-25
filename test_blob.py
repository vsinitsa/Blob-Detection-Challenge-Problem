import unittest
from Blob_Detection import run, readfile, find_count

class TestBlob(unittest.TestCase):
    def test_invalid_file(self):
        self.assertFalse(readfile("doesnotexist.txt"))

    def test_tiny_array(self):
        array = [["O"]]
        self.assertEqual(run(array), {"X": 0, "O": 1})

    def test_long_array(self):
        array = [["O", "X", "X", "X", "X", "O", "O"]]
        self.assertEqual(run(array), {"X": 4, "O": 2})

    def test_weird_pattern(self):
        array = [["O", "O", "O", "O", "O"], ["X", "X", "X", "X", "O"], ["O", "O", "O", "O", "O"], ["O", "X", "X", "X", "X"], ["O", "O", "O", "O", "O"]]
        self.assertEqual(run(array), {"X":4, "O": 17})

    def test_large_array(self):
        array = readfile("generate10x10.txt")
        self.assertEqual(run(array), {"X": 13, "O": 56})

    def test_normal_array(self):
        array = readfile("test.txt")
        self.assertEqual(run(array), {"X": 17, "O": 21})

    ''' to test that my recursive function worked I generated a large 50x50 array then picked a random point
    and counted how many x's were in that specific blob by hand'''
    def test_find_count(self):
        array = readfile("generate50x50.txt")
        self.assertEqual(find_count(41,8,41,8,"X", 0, array), 17)

if __name__ == '__main__':
    unittest.main()
