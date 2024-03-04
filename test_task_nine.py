from unittest import TestCase

import task_nine
from task_nine import count_letters_and_digits


class Test(TestCase):
    def test_collect_input_count_digit_and_sentence(self):
        user_input = 'Hello World! 123'
        result = task_nine.count_letters_and_digits(user_input)
        expected_result = (10, 3)
        self.assertEqual(result, expected_result)

    def test_collect_input_count_upper_and_lower_sentence(self):
        user_input = 'Hello World! 123'
        result = task_nine.count_upper_letters_and_lower_letter(user_input)
        expected_result = (2, 8)
        self.assertEqual(result, expected_result)


