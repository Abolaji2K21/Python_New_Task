# class Task_Seven:
#     def __init__(self, string_name):
#         self._string_name = string_name
#
#     @property
#     def string_name(self):
#         return self._string_name
#
#     @string_name.setter
#     def string_name(self, value):
#         self._string_name = value
#
#     @string_name.getter
#     def print_name(self):
#         return self._string_name
#
#
#
#
#
#
#
#     digits = list(range(1,51))
#
#     def check_even(number):
#         return number % 2 == 0
#
#     def raises_up(number):
#         return number ** 2
#
#
#
#     ass=list(filter(check_even, digits))
#     ass2=list(filter(lambda numbers: numbers % 2 == 0, digits))
#     ass3=list(map(raises_up,digits))
#     ass4=list(map(lambda numbers: numbers ** 2, digits))
#
#     print(ass)
#     print(ass2)
#     print(ass3)
#     print(ass4)

class Complex:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __add__(self, other):
        return f'{self.left + other.left}j {"+"} {self.right + other.right}i'
        # return Complex(self.left + other.left, self.right + other.right)

    def __sub__(self, other):
        return f'{self.left - other.left}j {"-"} {self.right - other.right}i'

    def __iadd__(self, other):
        self.left += other.left
        self.right += other.left
        return Complex(self.left, self.right)
        # return Complex(self.left + other.left, self.right + other.right)

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __gt__(self, other):
        return self.left >= other.left and self.right >= other.right

    def __lt__(self, other):
        return self.left <= other.left and self.right <= other.right

    def __repr__(self):
        return f'{self.left}j {"+" if self.right > 0 else "-"} {abs(self.right)}i'


c1 = Complex(2, 3)
print(c1)
c2 = Complex(5, -2)
print(c2)
print(c1 + c2)

c1 += c2

print(c1 - c2)
print(c1 == c2)
print(c2 > c1)
print(c2 < c1)
print(c1)

# c = 50
# h = 30
# output = []
#
# d = int(input("Kindly enter the value of d : "))
# q = (2 * 50 * d)
# first = q / 30
# result = int(first ** 0.5)
# print(result)
# output.append(result)
# print(output)

#
# write a program that calculates and prints the value according to the given formula Q = square root of [(2* c *
# d)/h] following are the fixed values of c and h: c is 50. h is 30 . d is the variable whose values should be input
# to your program in a comma- seperated sequence sample input : 100,150,180 sample output: 18 , 22, 24



