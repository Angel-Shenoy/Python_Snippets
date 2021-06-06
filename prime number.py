#!/usr/bin/env python
# coding: utf-8

# In[ ]:


number= int(input('Enter a number:'))
i=2
j=number//2
print(f"half of number is {j}")

for i in range(2,j+1):
    if number%i==0:
        print(f"{number} is divisible by {i}")
        break
    print(f"i is now {i}")    
        
print(f"final value of i = {i}") 
print(f"Number {number}")
if i==j:
    print(f"Number {number} is prime")
else:
    print(f"Number {number} is not prime")


# In[32]:


number= int(input('Enter a number :'))
i=2
j=number//2
for i in range(2,j+1):
    if number%i==0:
        break
if i==j:
    print(f"Number {number} is prime")
else:
    print(f"Number {number} is not prime")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




