#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import math

#angle=int(input("Angle?"))
r=int(input("radius?"))
n=int(input("petals?"))
angle=360/n
def polyline(t, n, length, angle):
    for i in range(n):
        
        t.fd(length)
        t.lt(angle)
ash=turtle.Turtle()
#polyline(ash,n,r,angle)
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
ash=turtle.Turtle()
def polygon(t, n, length):
    angle = 360/n
    polyline(t, n, length, angle)
#polygon(ash,n,100)
    
    

    
#arc(ash,100,180)

def petal(t,r,angle):
    angle=360/n
    
    arc(t,r,angle)
    t.lt(180-angle)
    arc(t,r,angle)
    
    
ash = turtle.Turtle()
#petal(ash,r, angle)


        



def flower(t,r,n,angle):

    for i in range(n):
    
        petal(t,r,angle)
        t.rt(180-angle)
    #petal(t,r,angle)
    #t.lt(angle)
    #petal(t,r,angle)
    #t.lt(angle)
    #petal(t,r,angle)
flower(ash,r,n,angle)


# In[ ]:




