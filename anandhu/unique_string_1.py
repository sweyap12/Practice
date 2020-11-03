"""
Verify that a string has only unique characters
"""

in_string = input("Enter String:")

# Pythonic
# if len(in_string) == len(set(in_string)):
#     print("Unique String")
# else:
#     print(f'{set(in_string)} is not equal to {in_string}')

#  2
# for pos, char in enumerate(in_string):
#     for num in range(pos+1, len(in_string)):
#         if char == in_string[num]:
#             print("Not Unique")
#             exit(0)
# print("Unique String")


# 3
char_dict = {}
for char in in_string:
    if not char_dict.get(char):
        char_dict[char] = 1
    else:
        print("Not Unique")
        exit(0)
print("Unique String")
