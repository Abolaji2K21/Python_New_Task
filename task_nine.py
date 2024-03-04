def count_letters_and_digits(sentence):
    num_letters = 0
    num_digits = 0

    for word in sentence:
        # for letter in word:
        if word.isalpha():
            num_letters += 1
        elif word.isdigit():
            num_digits += 1

    return num_letters, num_digits


def count_upper_letters_and_lower_letter(sentence):
    num_upper = 0
    num_lower = 0

    for word in sentence:
        # for letter in word:
        if word.isupper():
            num_upper += 1
        elif word.islower():
            num_lower += 1

    return num_upper, num_lower




# def main():
#     sentence = input("Enter a sentence: ")
#     letter_count, digit_count = count_letters_and_digits(sentence)
#     print("Number of letters:", letter_count)
#     print("Number of digits:", digit_count)
#
#
# if __name__ == "__main__":
#     main()
