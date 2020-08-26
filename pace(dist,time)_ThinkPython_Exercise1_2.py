#!/usr/bin/env python
# coding: utf-8

# In[11]:


### Think Python Exercise 1_2


# Q1
minutes=int(input("Minutes? "))
seconds=int(input("Seconds? "))

def sec(seconds,minutes):
    return (60*minutes) + seconds
time = sec(seconds,minutes)
#print(time)
print("{} minutes and {} seconds is equiavent to {} seconds".format(minutes,seconds,time))

# Q2
km=float(input("Kilometers? "))
def mile(km):
    return round(km/1.61,1)
#dist=mile(km)
print("{} km = {} miles".format(km,dist))

#Q3
def pace(dist,time):
    return round((time/60)/dist,1)
pace=pace(dist,time)
#print(pace)
def avspd(dist,time):
    return round(dist/(time/3600),1)
speed=avspd(dist,time)
#print(speed)
print("Your pace is {} minutes per mile, at an average speed of {} mph".format(pace, speed))


# In[ ]:




