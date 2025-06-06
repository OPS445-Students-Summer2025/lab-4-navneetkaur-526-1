#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(s):
    # Return the first five characters of the string argument s
    return s[:5]

def last_seven(s):
    # Return the last seven characters of the string argument s
    return s[-7:]

def middle_number(n):
    # Convert the number to string and return characters at index 1 and 2
    s = str(n)
    return s[1:3]

def first_three_last_three(s1, s2):
    # Return a string starting with first 3 chars of s1 and last 3 chars of s2
    return s1[:3] + s2[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
