numbers = [33, 7, 12, 45, 23, 5, 38, 19, 42, 8]
word = ["hannah", "beejay", "izu", "bolaji"]


def calculate_length(num):
    count = 0
    for index in num:
        count += 1
    return count

def sum_even_positions(num):
    total = 0
    for index in range(len(num)):
        if index % 2 == 0:
            total += num[index]
    return total

def sum_odd_positions(num):
    total_again = 0

    for index in range(len(num)):
        if index % 2 != 0:
            total_again +=num[index]
    return total_again


def average_of_all_Elements(num):
    sum_total = 0
    average = 10

    for index in range(len(num)):
        sum_total +=num[index]

    return sum_total / 10

def multiply_all_element_at_Third_positions(num):
    sum_again = 1;

    for index in range(2, len(num), 3):
        sum_again *= num[index]

    return sum_again

def maximum_number_from_the_list(num):
    maximum = num[0]

    for index in range(1, len(num)):
        if num[index] > maximum:
            maximum = num[index]

    return maximum


def minimum_number_from_the_list(num):
    minimum = num[0]

    for index in range(len(num)):
        if num[index] < minimum:
            minimum = num[index]
    return minimum

def list_of_String(words):
    result = []
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            result.append(word)
    return result
