"""
Program to verify that teo string are palindrome or not
"""

string_dict_1 = dict()
string_dict_2 = dict()

string_1 = input("Enter First String: ")
string_2 = input("Enter Second String: ")

for ch in string_1:
    if string_dict_1.get(ch) is None:
        string_dict_1[ch] = 1
        continue
    string_dict_1[ch] += 1

for ch in string_2:
    if string_dict_2.get(ch) is None:
        string_dict_2[ch] = 1
        continue
    string_dict_2[ch] += 1

if string_dict_1 == string_dict_2:
    print(f'{string_1} and {string_2} are palindromes')
else:
    print(f'{string_1} and {string_2} are NOT palindromes')