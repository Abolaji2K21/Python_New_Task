# class SevenSegment:
# #     def __init__(self):
# #         self.is_on = False
# #
# #     def display_segment(self, digits):
# #         self._validate(digits)
# #
# #         segment_patterns = {
# #             "11111101": "# # # #\n#     #\n#     #\n#     #\n# # # #",
# #             "01100001": "      #\n      #\n      #\n      #\n      #",
# #             "11011011": "# # # #\n      #\n# # # #\n#\n# # # #",
# #             "11110011": "# # # #\n      #\n# # # #\n      #\n# # # #",
# #             "01100111": "#     #\n#     #\n# # # #\n      #\n      #",
# #             "10110111": "# # # #\n#\n# # # #\n      #\n# # # #",
# #             "10111111": "# # # #\n#\n# # # #\n#     #\n# # # #",
# #             "11100001": "# # # #\n      #\n      #\n      #\n      #",
# #             "11111111": "# # # #\n#     #\n# # # #\n#     #\n# # # #",
# #             "11110111": "# # # #\n#     #\n# # # #\n      #\n# # # #"
# #
# #         }
# #         return segment_patterns.get(digits, "")
# #
# #     def _validate(self, numbers):
# #         if len(numbers) != 8:
# #             raise ValueError("Number must be 8 digits long")
# #         last_digit = numbers[7]
# #         if last_digit == '0':
# #             self.is_on = False
# #         elif last_digit == '1':
# #             self.is_on = True
# #         else:
# #             raise ValueError("Invalid last digit. Should be '0' or '1'.")
# #
# #     def is_on(self):
# #         return self.is_on
# #
# #
# # def main():
# #     segment = SevenSegment()
# #
# #     while True:
# #         user_input = input("Enter 8-digit binary number (or 'exit' to quit): ")
# #
# #         if user_input.lower() == 'exit':
# #             break
# #
# #         try:
# #             pattern = segment.display_segment(user_input)
# #             print("Segment pattern:")
# #             print(pattern)
# #         except ValueError as e:
# #             print("Invalid input:", e)
# #
# #
# # if __name__ == "__main__":
# #     main()
#
#
#     def display_seven_segment_of(binary_number):
#         check_input(binary_number)
#         return display_segment(binary_number)
#
#
#     def display_segment(binary_number):
#         bool_list = convert_input_to_boolean_list(binary_number)
#         horizontal = display_horizontal(bool_list[0])
#         vertical = display_vertical(bool_list[5], bool_list[1])
#         horizontal += display_horizontal(bool_list[6])
#         vertical += display_vertical(bool_list[4], bool_list[2])
#         horizontal += display_horizontal(bool_list[3])
#         return horizontal + '\n' + vertical
#
#
#     def check_input(user_input: str):
#         if len(user_input) != 8:
#             raise ValueError("Binary number must be 8 digits long")
#         if not all(char in '01' for char in user_input):
#             raise ValueError("Binary number must contain only 0's and 1's")
#
#
#     def display_horizontal(condition: bool):
#         return " # # # # #\n" if condition else ""
#
#
#     def display_vertical(condition1: bool, condition2: bool):
#         lines = []
#         if condition1 and condition2:
#             for _ in range(4):
#                 lines.append("#         #\n") 
#         elif condition1 and not condition2:
#             for _ in range(4):
#                 lines.append("#         \n")
#         elif not condition1 and condition2:
#             for _ in range(4):
#                 lines.append("         #\n")
#         return ''.join(lines)
#
#
#     def convert_input_to_boolean_list(binary_number: str) -> list:
#         return [char == '1' for char in binary_number]
#
