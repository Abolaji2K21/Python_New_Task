import unittest
from Seven_Segment import SevenSegment

class TestSevenSegment(unittest.TestCase):

    # def test_display_segment_zero(self):
    #     segment = SevenSegment()
    #     expected_pattern = """
    #                 # # # #
    #                 #     #
    #                 #     #
    #                 #     #
    #                 # # # #
    #                 """
    #     self.assertEqual(expected_pattern, segment.display_segment("11111101"))
    #     self.assertFalse(segment.is_on)
    #
    # def test_display_segment_one(self):
    #     segment = SevenSegment()
    #     expected_pattern = """
    #                       # # # #
    #                             #
    #                             #
    #                             #
    #                             #
    #                       """
    #     self.assertEqual(expected_pattern, segment.display_segment("11100001"))
    #     self.assertTrue(segment.is_on)

    def test_invalid_digit(self):
        segment = SevenSegment()
        with self.assertRaises(ValueError):
            segment.display_segment("1111111199")

    def test_invalid_length(self):
        segment = SevenSegment()
        with self.assertRaises(ValueError):
            segment.display_segment("1110001")

# unittest.main()