#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Hometime from a jog 



#Think Python O'Reilly
# p 19. Exercise 2-2
# Q3
# If I leave my house at 6:52am and run 1 mile at an speed 8.15 mph
# then 3 miles at 7.12 mph and then 1 mile again at 8.15mph.
# What time do I arrive home?
dep=str(input("Time in format of hour:min "))
#depart= str(dep)
depmin=dep.split(':')
depmins=int(depmin[0])*60 + int(depmin[1])
d1 = 1
d2 = 3
s1 = 8.15
s2 = 7.12
t1=d1/s1
t2=d2/s2
t1min=t1*60
t2min=t2*60
duration = int(2*t1min) + int(t2min)
arriv = depmins + duration

homehour = round(arriv//60,0)
homemin = round(arriv - homehour*60,0)
hometime=str(homehour) + ':' + str(homemin)
print('Home at {}:{}'.format(homehour,homemin) )


# The correct version is to define the speed as "pace", which reads as follows:
# "If I leave my house at 6:52am and run 1 mile at an easy pace (8:15 per mile)
# then 3 miles at 7:12 per and then 1 mile again at (8:15 per mile).
# What time to I arrive home?""

dep=str(input("Time? "))
depart= str(dep)
#depart= str('6:52')
depmin=depart.split(':')
depmins=int(depmin[0])*60 + int(depmin[1])

d1 = 1
d2 = 3


p1 = str('8:15')
p1min = p1.split(':')
p1mins=int(p1min[0])+int(p1min[1])/60

p2 = str('7:12')
p2min = p2.split(':')
p2mins=int(p2min[0])+int(p2min[1])/60

t1=d1*p1mins
t2=d2*p2mins

duration = int(2*t1) + int(t2)
arriv = depmins + duration

homehour = round(arriv//60,0)
homemin = round(arriv - homehour*60)
hometime=str(homehour) + ':' + str(homemin)
print('Home at {}:{}'.format(homehour,homemin) )




# The alternative is to define the speed as "pace"


# In[23]:


p2mins


# In[31]:


t1


# In[32]:


t2


# In[ ]:




