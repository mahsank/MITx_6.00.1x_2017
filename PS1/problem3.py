'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters
occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your
program should print

Longest substring in alphabetical order is: beggh In the case of ties, print
the first substring. For example, if s = 'abcbcd', then your program should
print

Longest substring in alphabetical order is: abc

'''

char, temp, found = '', '', ''

#s = 'azcbobobegghakl'

for letter in s:
    if letter >= char:
        temp += letter
    else:
        temp = letter
    if len(temp) > len(found):
        found = temp
    char = letter

print("Longest substring in alphabetical order is: " + found)
