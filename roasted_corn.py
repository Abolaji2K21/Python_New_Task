result = "google.com"
print(f'{"G-"}{result.count("g")} {" O-"}{result.count("o")} {" L-"}{result.count("l")} {" E-"}{result.count("e")} {" C-"}{result.count("c")} {" M-"}{result.count("m")}')

result = "google.com"
char_count = {}

for char in result:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(f"{char_count}")


sample = "google.com"
print({k: sample.count(k) for k in sample})


sample_list = "semicolon"
print({i: sample_list.count(i) for i in sample_list})





