#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# C3 FUNCTIONS
# Exercise 3.1
# 
# Write a function names right_justify that takes a string named 's' as a parameter
# and prints the string with enough leading spaces so that the first letter of the string is in
# column 70 of the display


#right_justify_v1

# Version 1 places the last letter in column 70

s=str(input("Enter word "))    

def right_justify(s):
    print(s)
    print(s)
right_justify(" "*70 + s)

#########################


# In[ ]:




