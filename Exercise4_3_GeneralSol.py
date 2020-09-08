#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import math
lyra = turtle.Turtle()
n=int(input("Number of sides? "))
r=int(input("Radius of side? "))
#angles
A=(360/n)
Arad=(360/n)*(math.pi/180)
B=90+(360/(2*n))
C=90+(360/(2*n))
b=r
c=r

Z=(math.cos(Arad))

a=(math.sqrt(((b**2)+(c**2)-(2*b*c*Z))    ))
#a=(c*math.sin(A))/(math.sin(C))

"""Defines the triangle"""
def square(t):
    
    t.lt(A)
    t.fd(b)
    t.rt(B)
    t.fd(a)
    t.rt(C)
    t.fd(c)
#square(lyra)

"""defines the direction for the consecutive triangles"""
def rotate(t):
    square(t)
    t.lt(180-A)
    
    
#rotate(lyra)
"""Repeats the creation of triangles"""
def combine(t):
    for i in range(n):
        rotate(t)
combine(lyra)


# In[ ]:


A


# In[ ]:


B


# In[ ]:




