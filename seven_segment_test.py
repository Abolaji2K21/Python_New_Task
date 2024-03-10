import unittest
from Exception.invalid_input_exception import InvalidInputException
from Exception.invalid_length_exception import InvalidLengthException
from seven_segment import SevenSegment


class TestSevenSegment(unittest.TestCase):
    def test_convert_string_input_valid_input_return_segments(self):
        segment = SevenSegment()
        input_str = "11111111"
        segments = segment.convert_string_input(input_str)
        self.assertListEqual([True, True, True, True, True, True, True, True], segments)

    def test_convert_string_input_invalid_input_throw_invalid_input_exception(self):
        segment = SevenSegment()
        input_str = "01234567"
        with self.assertRaises(InvalidInputException):
            segment.convert_string_input(input_str)

    def test_convert_string_input_invalid_length_throw_invalid_length_exception(self):
        segment = SevenSegment()
        input_str = "111111111"
        with self.assertRaises(InvalidLengthException):
            segment.convert_string_input(input_str)

    def test_convert_string_input_empty_input_throw_invalid_length_exception(self):
        segment = SevenSegment()
        input_str = ""
        with self.assertRaises(InvalidLengthException):
            segment.convert_string_input(input_str)

    def test_convert_string_input_length_less_than_eight_throw_invalid_length_exception(self):
        segment = SevenSegment()
        input_str = "1111"
        with self.assertRaises(InvalidLengthException):
            segment.convert_string_input(input_str)

    def test_convert_string_input_input_with_spaces_throw_invalid_input_exception(self):
        segment = SevenSegment()
        input_str = "1 1 1 1 1 1 1 1"
        with self.assertRaises(InvalidInputException):
            segment.convert_string_input(input_str)

    def test_convert_string_input_input_with_other_symbols_throw_invalid_input_exception(self):
        segment = SevenSegment()
        input_str = "11@11111"
        with self.assertRaises(InvalidInputException):
            segment.convert_string_input(input_str)

    def test_convert_string_input_invalid_character_throw_invalid_input_exception(self):
        segment = SevenSegment()
        input_str = "11A11111"
        with self.assertRaises(InvalidInputException):
            segment.convert_string_input(input_str)

    def test_convert_string_input_all_segments_off_return_all_false(self):
        segment = SevenSegment()
        input_str = "00000000"
        segments = segment.convert_string_input(input_str)
        self.assertListEqual([False, False, False, False, False, False, False, False], segments)

    def test_convert_string_input_mixed_input_return_segments(self):
        segment = SevenSegment()
        input_str = "10011001"
        segments = segment.convert_string_input(input_str)
        self.assertListEqual([True, False, False, True, True, False, False, True], segments)

    # def test_display_seven_segment(self):
    #     segment = SevenSegment()
    #
    #     expected_all_on = """\
    #                 # # # #
    #                 #     #
    #                 #     #
    #                 #     #
    #                 # # # #
    #                 #     #
    #                 #     #
    #                 #     #
    #                 # # # #"""
    #     self.assertEqual(expected_all_on, segment.display_seven_segment("11111111"))


