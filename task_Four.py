def intersperse_strings(str1, str2):
    return str2[0:2] + str1[2::] + ' ' + str1[0:2] + str2[2::]


def swapping_strings(string1,string2):
    string1 = ''
    string2 = ''
    char_list = list(string1 + string2)
