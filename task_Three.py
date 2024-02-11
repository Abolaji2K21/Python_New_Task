def creation_of_my_list(num):
    numbers = list(range(1, 15))
    return numbers


def duplication_of_my_list(num):
    numbers = list(range(1, 15))
    return numbers, numbers * 2


def eliminate_duplicate_list(num):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    duplication_of_my_list(numbers)
    unique_numbers = list(set(numbers))
    return unique_numbers


def add_every_third_element(numbers):
    total = 0
    count = 1
    for num in numbers:
        if count % 3 == 0:
            total += num
        count += 1
    return total


def add_the_first_middle_last(numbers):
    length = len(numbers)

    first_num = numbers[0]
    last_num = numbers[-1]

    if length % 2 != 0:
        middle_num = numbers[length // 2]
    else:
        middle1 = numbers[length // 2 - 1]
        middle2 = numbers[length // 2]
        middle_num = (middle2 + middle1) / 2

    return first_num + last_num + middle_num


# def collection_of_unique_elements():
#   numbers = set()

#  for num in range(1, 11):
#   numbers.add(num)
# return numbers


# print(collection_of_unique_elements())


def sum_collection(numbers):
    total = 0
    for num in set(numbers):
        total += num
    return total


def remove_item(numbers, element):
    if element in set(numbers):
        numbers.remove(element)
        return element
    else:
        return None


def find_interception(num, numbers):
    set_num = set(num)
    set_numbers = set(numbers)

    return set_num.intersection(set_numbers)



