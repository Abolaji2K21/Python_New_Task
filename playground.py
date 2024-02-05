def ascending_function(lst):
    for check in range(len(lst)):
        for count in range(check + 1 , len(lst)):
            if lst[check] > lst[count]:
                lst[check], lst[count] = lst[count], lst[check]
    return lst


def descending_function(lst):
    for check in range(len(lst)):
        for count in range(check + 1 , len(lst)):
            if lst[check] < lst[count]:
                lst[check], lst[count] = lst[count], lst[check]
    return lst


def search_key(data: list, key: int) -> int:
    for index, value in enumerate(data):
        if value == key:
            return index
    return -1


