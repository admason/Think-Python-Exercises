#!/usr/bin/env python
# coding: utf-8

# In[ ]:


col = int(input("number of columns? "))


top=    '+' + 4*'-'
lside='|    '
rside='|'
base=   '+' + 4*'-' 

def grid(func,arg):
    print(col*top+' '+' +')
    print(lside+col*rside)

def double(func,arg):
    func(arg)
    func(arg)    
    
def quad(func,arg):
    double(func,arg)
    double(func,arg)    

def grid(func,arg):
    print(col*top +  '+')
    quad(print,(lside )*col + rside )
    
def twicegrid(func,arg):
    grid(print,''*col)
    print(col*base+'+')
   
def fourgrid(func,arg):
    grid(print,''*col)
    grid(print,''*col)
    grid(print,''*col)
    grid(print,''*col)
    print(col*base+'+')

#(grid(print,''))
#twicegrid(print,'')
fourgrid(print,'')


# In[ ]:







# In[ ]:




