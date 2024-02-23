from time import time


def decorate(sh):
    print("********")
    print(sh())
    print("********")


@decorate
def show_name():
    return "Miriam"


def decorate2(sh):
    def inner(*args, **kwargs):
        print("********")
        print(sh(*args, **kwargs))
        print("********")

    return inner


@decorate2
def show_name(name):
    return name


show_name(name="Omi ewa")


def time_taken(func):
    def wrap(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"it took {t1 - t2: 3f} ms to execute")
        return result

    return wrap


@time_taken
def get_list(numbers):
    result = []
    for i in range(numbers):
        result.append(i)
    return result


get_list(1000000)
