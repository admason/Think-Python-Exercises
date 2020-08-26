#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Think Python Exercise 2_2


# Q2

# Book Cost
# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs are $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?

# Adapt the code to accept any cover cost and any quantity

cover=float(input("Cover cost?"))
disc=0.4
ship=3
sship=0.75
qty=int(input("Quantity? "))

if qty==1:
   cost=qty*cover*(1-disc)+(qty*ship) 
else:
    #cost=(qty-1)*cover*(1-disc)+((qty-1)*sship)+ship 
    cost=(cover*(1-disc)+ship)+(cover*((qty-1)*(1-disc)*sship))

bookcost=str(round(cost,2))
print('Wholesale price for ' + str(qty) + ' copies is $ ' + bookcost)


# In[ ]:




