# count = 0
# count1 = 0
# for num in range(1, number):
#     if num % 2 == 0:
#         count += num
#     else:
#         count1 += num

# even = sum([num for num in range(number) if num % 2 == 0])
# odd = sum([num for num in range(number) if num % 2 != 0])
# print(even)
# print(odd)

try:
    number = int(input('Enter Number Of Your Choice : '))
    print(f"Sum of even numbers is {sum(list(range(1, number))[1::2])}")
    print(sum(list(range(1, number))[0::2]))

except ValueError:
    print("invalid input")
except TypeError:
    print("Day_o")
