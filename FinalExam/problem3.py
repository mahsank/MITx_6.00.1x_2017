'''
Implement a function that meets the specifications below.

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
For example, sum_digits("a;35d4") returns 12.

'''

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """

    str_list = list(s)
    count = 0
    for i in str_list:
        if i.isdigit():
            count += int(i)
    if s != '0' and count == 0:
        raise ValueError()
    else:
        return count

