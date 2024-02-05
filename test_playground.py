import unittest
import playground


class TestAscendingFunction(unittest.TestCase):
    def test_that_function_is_not_none(self):
        self.assertIsNotNone(playground.ascending_function)

    def test_that_function_sort_array_in_ascending_order(self):
        sample_list = [10, 2, 8, 9, 3, 4, 1, 5]
        sample_output = [1, 2, 3, 4, 5, 8, 9, 10]
        (self.assertEqual
         (playground.ascending_function(sample_list), sample_output))

class TestDescendingFunction(unittest.TestCase):
    def test_that_function_sort_array_in_descending_order(self):
        sample_list = [10, 2, 8, 9, 3, 4, 1, 5]
        sample_output = [10, 9, 8, 5, 4, 3, 2, 1]
        (self.assertEqual
         (playground.descending_function(sample_list), sample_output))

class TestThatKeyIsPresentFunction(unittest.TestCase):
    def test_that_function_key_Is_not_None(self):
        self.assertIsNotNone(playground.search_key)


    def test_that_Key_exist(self):
        sample_list = [10, 2, 8, 9, 3, 4, 1, 5]
        self.assertEqual(2, playground.search_key(sample_list, 8))
        self.assertEqual(5, playground.search_key(sample_list, 4))

    def test_that_Key_does_not_exist(self):
        sample_list = [10, 2, 8, 9, 3, 4, 1, 5]
        self.assertEqual(-1, playground.search_key(sample_list, 7))
        self.assertEqual(-1, playground.search_key(sample_list, 6
                                                   ))

