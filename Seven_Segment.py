class SevenSegment:
    def __init__(self):
        self.is_on = False

    def display_segment(self, digits):
        self._validate(digits)

        segment_patterns = {
            "11111101": """
                        # # # #
                        #     #
                        #     #
                        #     #
                        # # # #
                        """,
            "01100001": """
                               #
                               #
                               #
                               #
                               #
                       """,
            "11011011": """
                        # # # #
                              #
                        # # # #
                        #
                        # # # #
                       """,
            "11110011": """
                        # # # #
                              #
                        # # # #
                              #
                        # # # #
                       """,
            "01100111": """
                        #     #
                        #     #
                        # # # #
                              #
                              #
                       """,
            "10110111": """
                        # # # #
                        #
                        # # # #
                              #
                        # # # #
                       """,
            "10111111": """
                        # # # #
                        #
                        # # # #
                        #     #
                        # # # #
                       """,
            "11100001": """
                      # # # #
                            #
                            #
                            #
                            #
                      """,
            "11111111": """
                        # # # #
                        #     #
                        # # # #
                        #     #
                        # # # #
                       """,
            "11110111": """
                        # # # #
                        #     #
                        # # # #
                              #
                        # # # #
                       """
        }
        return segment_patterns.get(digits, "")

    def _validate(self, numbers):
        if len(numbers) != 8:
            raise ValueError("Number must be 8 digits long")
        last_digit = numbers[7]
        if last_digit == '0':
            self.is_on = False
        elif last_digit == '1':
            self.is_on = True
        else:
            raise ValueError("Invalid last digit. Should be '0' or '1'.")

    def is_on(self):
        return self.is_on


def main():
    segment = SevenSegment()

    while True:
        user_input = input("Enter 8-digit binary number (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break

        try:
            pattern = segment.display_segment(user_input)
            print("Segment pattern:")
            print(pattern)
        except ValueError as e:
            print("Invalid input:", e)


if __name__ == "__main__":
    main()
