#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#right_justify_v2

# # Version 2 subtracts the length of s and places the last letter in column 70

s=str(input("Enter word "))

def right_justify(s):
    print(s)
    print(s)
rj(" "*(70-len(s)) + s)

