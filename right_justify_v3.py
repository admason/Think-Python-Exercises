#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#right_justify_v3


# A tweak to the code allows the user to define in which column the
# last letter will be situated, defined by the input "col"

s=str(input("Enter word "))
col = int(input("Column placement of last letter? "))
def right_justify(s):
    print(s)
    print(s)
rj(" "*(col-len(s)) + s)

