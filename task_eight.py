import math


def calculate_Q(d):
    c = 50
    h = 30
    return int(math.sqrt((2 * c * d) / h))


d_values = input("Enter comma-separated values of d: ").split(',')

result = [calculate_Q(int(d)) for d in d_values]

print("Sample output:", ', '.join(map(str, result)))





