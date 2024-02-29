# name1 = "bolaji"
# name3 = "chichi"
# name2 = "dayo"
#
# print(name1 == name2)
# print(name1 < name2)
# print("c" in name3)
# print("c,i,h" in name3)
# print("b" or "f" in name1 )
# print(f'[{name1:>10}]')
# print(f'[{name1:<10}]')
# print(f'[{name1:^10}]')
# print(f'[{name1:>10}]   [{name2:<10}]')
#
# print(f'{name1} {name2} {name3}')
#
# name = name1 + name2 + name3
# print(f'{name} {" "}')
#
# print(name1 * 5)
#
# name4 = "   muhammed  "
# print(name4.strip())
# print(name4)
#
# print(name3.capitalize())
# print(name2.upper())
#
# sentence = "welcome to semic colon . you are in a safe hands "
#
# print(sentence.capitalize())
# print(sentence.title())
# print(sentence.casefold())
# print(sentence.swapcase())
# print(sentence.count("e"))
# print(sentence.index("e"))
# print(sentence.rindex("e"))
#
# names = input().strip()
# if names.isalpha():
#     print("valid name")
# else:
#     print("invalid name")
#
# names = input().strip()
# if names.isalnum():
#     print("valid name")
# else:
#     print("invalid name")
#
# nama = ["ayo", "tayo", "shayo"]
# print(" -name- ".join(nama))
# print(sentence.replace("a", "x"))





# Sentence1 = "the palace is few miles away from the village but going to the palace to see startups is cool and fun "
# print('the :',Sentence1.count("the"))
# print('palace :',Sentence1.count("palace"))
# print('is :',Sentence1.count("is"))
# print('few :',Sentence1.count("few"))
#
# print('miles: ',Sentence1.count("miles"))
# print('away:',Sentence1.count("away"))
# print('from',Sentence1.count("from"))
# print('village:',Sentence1.count("village"))
# print('but:',Sentence1.count("but"))
# print('going:',Sentence1.count("going"))
# print('to:',Sentence1.count("to"))
# print('see:',Sentence1.count("see"))
# print('startup:',Sentence1.count("startup"))
# print('cool:',Sentence1.count("cool"))
# print('and:',Sentence1.count("and"))
# print('fun:',Sentence1.count("fun"))


sentence2 = "the palace is few miles away from the village but going to the palace to see startups is cool and fun"
words_of_interest = {"the", "palace", "is", "few", "miles", "away", "from", "village", "but", "going", "to", "see", "startup", "cool", "and", "fun"}

for word in words_of_interest:
    print(word + ":", sentence2.count(word))




