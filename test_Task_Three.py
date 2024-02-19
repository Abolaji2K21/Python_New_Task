import unittest
from unittest import TestCase

import task_Three


class MyTestCase(unittest.TestCase):
    def test_that_a_sequential_list_is_created(self):
        prototype = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertTrue(task_Three.creation_of_my_list(prototype))

    def test_that_a_duplicate_element_is_in_my_list(self):
        prototype = [1, 3, 2, 2, 1, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15,
                     15]
        self.assertTrue(task_Three.duplication_of_my_list(prototype))

    def test_eliminate_duplicate_list(self):
        prototype = [1, 3, 2, 2, 1, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15,
                     15]
        result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(result, task_Three.eliminate_duplicate_list(prototype))

    def test_add_every_third_element(self):
        prototype = [1, 2, 10, 4, 5, 10, 7, 8, 9]
        result = 29
        self.assertEqual(result, task_Three.add_every_third_element(prototype))

    def test_add_the_first_middle_last(self):
        prototype = [1, 2, 10, 4, 5, 5, 10, 7, 8, 10]
        result = 16
        self.assertEqual(result, task_Three.add_the_first_middle_last(prototype))

    def test_sum_collection(self):
        prototype = (1, 2, 10, 4, 5, 5, 10, 10)
        result = 22
        self.assertEqual(result, task_Three.sum_collection(prototype))

    def test_remove_item(self):
        prototype = {1, 2, 3, 4, 5, 6, 8, 10}
        element = 5
        result = 5
        self.assertEqual(result, task_Three.remove_item(prototype, element))

    def test_find_interception(self):
        prototype = {1, 2, 3, 4, 5, 6, 8, 10}
        prototype1 = {11, 2, 3, 14, 5, 16, 8, 10}
        result = {2, 3, 5, 8, 10}
        self.assertEqual(result, task_Three.find_interception(prototype, prototype1))
