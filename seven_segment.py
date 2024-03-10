from Exception.invalid_input_exception import InvalidInputException
from Exception.invalid_length_exception import InvalidLengthException


class SevenSegment:
    def __init__(self):
        self.segments = [False] * 8

    def draw_horizontal_line(self):
        return "# # # #"

    def draw_vertical_line_on_the_left(self):
        return """
               #
               #
               #"""

    def draw_vertical_line_on_the_right(self):
        return """
                       #
                       #
                       #"""

    def draw_vertical_line_on_both_sides(self):
        return """
               #     #
               #     #
               #     #"""

    def return_vertical_segments(self, left_switch, right_switch):
        if left_switch and right_switch:
            return self.draw_vertical_line_on_both_sides()
        elif not left_switch and right_switch:
            return self.draw_vertical_line_on_the_right()
        else:
            return self.draw_vertical_line_on_the_left()

    def return_horizontal_segments(self, top_switch):
        if top_switch:
            return self.draw_horizontal_line()
        else:
            return ""

    def validate_input(self, input_str):
        for char in input_str:
            if char not in ['0', '1']:
                raise InvalidInputException("Invalid Input: Only 0s and 1s are allowed.")

    def validate_length(self, input_str):
        if len(input_str) != 8:
            raise InvalidLengthException("The length of your input should be exactly eight")

    def convert_string_input(self, input_str):
        self.validate_input(input_str)
        self.validate_length(input_str)

        self.segments = [char == '1' for char in input_str]

        return self.segments

    def display_seven_segment(self, input_str):
        array = self.convert_string_input(input_str)

        if not array[7]:
            return ""

        return (self.return_horizontal_segments(array[0]) + "\n" +
                self.return_vertical_segments(array[5], array[1]) + "\n" +
                self.return_horizontal_segments(array[6]) + "\n" +
                self.return_vertical_segments(array[4], array[2]) + "\n" +
                self.return_horizontal_segments(array[3]))

