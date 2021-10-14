#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# In[2]:


import numpy as np

print('Test')
# This repo contains an introduction to [Jupyter](https://jupyter.org) and [IPython](https://ipython.org).
# 
# Outline of some basics:
# 
# * [Notebook Basics](../examples/Notebook/Notebook%20Basics.ipynb)
# * [IPython - beyond plain python](../examples/IPython%20Kernel/Beyond%20Plain%20Python.ipynb)
# * [Markdown Cells](../examples/Notebook/Working%20With%20Markdown%20Cells.ipynb)
# * [Rich Display System](../examples/IPython%20Kernel/Rich%20Output.ipynb)
# * [Custom Display logic](../examples/IPython%20Kernel/Custom%20Display%20Logic.ipynb)
# * [Running a Secure Public Notebook Server](../examples/Notebook/Running%20the%20Notebook%20Server.ipynb#Securing-the-notebook-server)
# * [How Jupyter works](../examples/Notebook/Multiple%20Languages%2C%20Frontends.ipynb) to run code in different languages.

# In[18]:


x = np.array([12,25,37])
y = np.array([59,63,71])
print (x+y) #Addition
print (x-y) #Substraction
print (x*y) #Multiplication


# In[19]:


print (x/y) #Division with float as output
print (x//y) #Division with integer as output


# In[20]:


print(np.dot(x,y)) #Dot operation
print(np.cross(x,y)) #Cross operation


# In[21]:


print(np.sqrt((x*x).sum())) # Modulus of list X(Doing the sum of the list X)
print(np.sqrt(y*y).sum()) #Modulus of list Y(Doing the sum of the list Y)



# In[24]:


print(np.exp(x)) #Exponential function on array X
print(np.exp(y)) #Exponential function on array Y


# In[25]:


print (np.log(x)) #Log function on array X
print (np.log(y)) #Log function on array Y


# In[ ]:




