import unittest
from Seven_Segment import SevenSegment, display_seven_segment_of


class TestSevenSegment(unittest.TestCase):

    def test_display_seven_segment_of(self):
        assert display_seven_segment_of("11111111") == \
               " # # # # #\n#         #\n # # # # #\n#         #\n # # # # #\n"
        # self.assertEqual(expected_pattern, segment.display_segment("11111101"))
        # self.assertFalse(segment.is_on)

    def test_invalid_digit(self):
        segment = SevenSegment()
        with self.assertRaises(ValueError):
            segment.display_segment("1111111199")

    def test_invalid_length(self):
        segment = SevenSegment()
        with self.assertRaises(ValueError):
            segment.display_segment("1110001")

    def test_that_my_app_is_truly_on(self):
        mySegment = SevenSegment()
        mySegment.display_segment("11100001")
        self.assertTrue(mySegment.is_on)

    def test_that_my_is_truly_off(self):
        mySegment = SevenSegment()
        mySegment.display_segment("11100000")
        self.assertFalse(mySegment.is_on)


unittest.main()
