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


    def __add__(self,other):
        return f'{self.left + other.left}j {"+"} {self.right + other.right}i'
        return Complex(self.left + other.left, self.right + other.right)

    def __sub__(self, other):
        return f'{self.left - other.left}j {"-"} {self.right - other.right}i'

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __gt__(self, other):
        return self.left >= other.left and self.right >= other.right

    def __lt__(self, other):
        return self.left <= other.left and self.righ <= other.right





    def __repr__(self):
        return f'{self.left}j {"+" if self.right > 0 else "-"} {abs(self.right)}i'

c1 = Complex(2,3)
print(c1)
c2 = Complex(5,-2)
print(c2)
print(c1 + c2)

print(c1 - c2)
print(c1==c2)
print(c2 > c1)
print(c2 < c1)














