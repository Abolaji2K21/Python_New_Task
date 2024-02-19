import unittest

import task_One

class MyTestCase(unittest.TestCase):

    def test_that_we_can_get_list_length(self):
        protoType = [1, 4, 5, 7, 7, 8, 8, 9, 9, 0]
        self.assertEqual(10, task_One.calculate_length(protoType))

    def test_that_we_can_sum_at_even_position(self):
        protoType = [1, 4, 5, 7, 7, 8, 8, 9, 9, 0]
        result = 30
        self.assertEqual(result, task_One.sum_even_positions(protoType))

    def test_that_we_can_sum_at_odd_position(self):
        protoType = [1, 4, 5, 7, 7, 8, 8, 9, 9, 0]
        result = 28
        self.assertEqual(result, task_One.sum_odd_positions(protoType))

    def test_that_we_can_get_average_num_from_the_list(self):
        protoType = [1, 4, 5, 7, 7, 8, 8, 9, 9, 0]
        result = 58 / 10
        self.assertEqual(result, task_One.average_of_all_Elements(protoType))

    def test_that_we_can_get_multiple_of_all_element_at_Third_positions(self):
        protoType = [1, 4, 5, 7, 7, 8, 8, 9, 9, 0]
        result = 360
        self.assertEqual(result, task_One.multiply_all_element_at_Third_positions(protoType))

    def test_that_we_can_get_the_maximum(self):
        protoType = [1, 4, 5, 7, 7, 8, 8, 9, 9, 0]
        result = 9
        self.assertEqual(result, task_One.maximum_number_from_the_list(protoType))

    def test_that_we_can_get_the_minimum(self):
            protoType = [1, 4, 5, 7, 7, 8, 8, 9, 9, 0]
            result = 0
            self.assertEqual(result, task_One.minimum_number_from_the_list(protoType))

    def test_that_we_can_get_the_list_of_Strings(self):
            protoType = ["hannah", "beejay", "izu", "bolaji","miriam"]
            result = ["hannah", "miriam"]
            self.assertEqual(result, task_One.list_of_String(protoType))




