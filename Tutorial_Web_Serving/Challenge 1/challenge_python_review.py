# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 17:50:07 2023

@author: lengu
"""

import math

def print_squares(a):
    for i in range(1, a + 1):
        print(i**2)

"""
The function print_squares functions by taking an input a
and running a for loop from 1 to a + 1 all the while squaring that value
"""

def average(input):

    if len(input) == 0:
        return 0
    for element in input:
        x = type(element)
        if x == str():
            return print("None")
    for element in input:
        try:
            int(element)
        except ValueError:
            return print("None")
    total = float(sum(input))    
    av = total / len(input)
    
    
    return av

"""
The function average() first of all checks whether the length of the input is 0
or contains any strings. If the input is of length 0, it manually returns a 0 
in order to prevent a division by 0 error. If the input contains a string, it 
prints "None" to recognize that an invalid input has been passed.
After checking that all the values in the list are numbers, the actual math 
of the function is done by converting the input to a float so that decimal places
can be reached, and then dividing the sum of the list by the length
"""





def is_prime(n): #Assumption is that n is a positive integer
    for i in range(2,n):
        if n % i == 0:
            return False

    return True
    

def prime_100(length): #Returns a list of the first 100 prime numbers
    for i in range(length):
        x = is_prime(i)
        if x == True:
            print(i)
        return
        
def count_letters(string):
    lstring = string.lower()
    lstring.count('a')
    return
"""
First of all, this function turns all of the string lowercase using the lower()
function
"""
    
def filter_strings(string):
     vowels = ["a" , "e" , "i" , "o" , "u"]
     count = 0
     for character in string:
         if character in vowels:
             count += 1
             
     if character >= 5:
        if count >= 1:
            return string         
        return

if __name__ == '__main__': # testcases
    prime_100(100)