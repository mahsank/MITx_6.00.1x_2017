'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2

'''

temp = 0 count = 0

#s = 'azcbobobegghakl'

string_len = len('bob') s_len = len(s)

for i in range(temp,s_len):
    if temp <= s_len - string_len:
        if s[temp:temp+string_len] == 'bob':
            count += 1
        temp += 1

print('Number of times bob occurs is : ' + str(count))
