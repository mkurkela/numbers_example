from unittest import TestCase
import os

from numbers import Numbers


class TestNumbers(TestCase):

    def setUp(self):
        '''
        Remove test_number_file if it exist before test case
        '''
        if os.path.isfile('test_number_file.txt'):
            os.remove('test_number_file.txt')

        # Test that test method works
        self.assertTrue(self.file_contains_n_unique_number(100, "verified_number_file.txt"))

    def tearDown(self):
        '''
        Remove test_number_file if it exist after test case
        '''

    @staticmethod
    def file_contains_n_unique_number(n, file_name):
        '''
        Verify that a file contains n unique numbers written line by line
        :param n: Count of numbers to checked
        :param file_name: The file under test
        :return: True if file has n amount of unique integers and nothing else
        '''
        if not os.path.isfile(file_name):
            return False

        read_list = []
        line_count = 0
        with open(file_name, 'r') as r_file:
            for line in r_file:
                line_count = line_count + 1
                if int(line) and line not in read_list:
                    read_list.append(line)

        if n != line_count:
            return False

        if len(read_list) == n:
            return True

    def test_write_numbers(self):
        # Test negative count
        self.assertFalse(Numbers.write_numbers(-1, "test_number_file.txt"), "Negative count accepted")

        # Test empty file name
        self.assertFalse(Numbers.write_numbers(100, ""), "Empty file name is not handled correctly")

        # Test valid write
        self.assertTrue(Numbers.write_numbers(100, "test_number_file.txt"),
                        "Writing 100 numbers to test_number_file.txt did not return true")
        self.assertTrue(self.file_contains_n_unique_number(100, "test_number_file.txt"),
                        "The file does not contain 100 unique numbers")

    def test_read_numbers(self):
        # Test empty file name
        self.assertIsNone(Numbers.read_numbers(50, ""),
                         "Empty file name is not handled correctly")

        # Test that negative count can't be given
        self.assertIsNone(Numbers.read_numbers(-1, "verified_number_file.txt"),
                         "Negative number count is not handled correctly")

        # Test that not more items than in file can be read
        self.assertFalse(Numbers.read_numbers(101, "verified_number_file.txt"),
                         "Read 101 numbers from file that contains only 100 numbers")

        # Test that numbers can also be read from files which contains also something else than integers
        read_list = Numbers.read_numbers(10, "test_mixed_number_file.txt")
        self.assertIsNotNone(read_list, "Mixed  number list returned None")
        self.assertEqual(len(read_list), len(set(read_list)),
                         "Items were not unique")
        self.assertEqual(10,len(read_list),
        "List lenght should be 10")

        # Test that doulbes are not accepted
        self.assertIsNone(Numbers.read_numbers(10, "test_float_file.txt"),
                          "Read doubles from file")

        # Test that file which contains same integers can not be read
        self.assertIsNone(Numbers.read_numbers(10, "test_same_number.txt"),
                          "Read same number")

        # Test that 50 unique integer was read
        read_list = Numbers.read_numbers(50, "verified_number_file.txt")
        self.assertIsNotNone(read_list,
                             "Read list from verified number file is None")
        self.assertEqual(50, len(read_list),
                         "List length should be 50")
        self.assertEqual(len(read_list), len(set(read_list)),
                        "Items were not unique")


    def test_is_integer(self):
        self.assertTrue(Numbers.check_integer(1))
        self.assertTrue(Numbers.check_integer(0))
        self.assertTrue(Numbers.check_integer(-1))
        self.assertTrue(Numbers.check_integer(1.0))
        self.assertFalse(Numbers.check_integer(1.2))
        self.assertFalse(Numbers.check_integer('string'))
        self.assertFalse(Numbers.check_integer('string with number 1'))
        self.assertFalse(Numbers.check_integer('a'))
