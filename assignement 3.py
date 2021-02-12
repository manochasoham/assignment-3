#!/usr/bin/env python
# coding: utf-8

# In[10]:


num=int(input("enter a number:"))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(f"{num}not a prime number")
            break
    else:
        print(num,"is a prime number")
            
else:
    print("not a prime number")


# In[ ]:





# In[ ]:




