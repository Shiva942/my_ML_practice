#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# In[ ]:


#Basic Fibonacci Series
var = int(input("NO OF FIBONACCI SERIES"))
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n-1)+fib(n-2)
for i in range (1,var+1):
    print (fib(i))

print('Hello')
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

# In[ ]:


#Fibonacci series with Memorizing power
cache={}

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        val = fib(n-1)+fib(n-2)
        cache[n] = val
        return val
    elif n in cache:
        return cache[n]

var = int(input("NO OF FIBONACCI SERIES"))
for n in range (1,var+1):
    print(fib(n))


# You can also get this tutorial and run it on your laptop:
# 
#     git clone https://github.com/ipython/ipython-in-depth
# 
# Install IPython and Jupyter:
# 
# with [conda](https://www.anaconda.com/download):
# 
#     conda install ipython jupyter
# 
# with pip:
# 
#     # first, always upgrade pip!
#     pip install --upgrade pip
#     pip install --upgrade ipython jupyter
# 
# Start the notebook in the tutorial directory:
# 
#     cd ipython-in-depth
#     jupyter notebook

# In[ ]:


#Fibonnaci series using the in-built LRU_Cache
from functools import lru_cache

@Lru_cache
def fib(n):
    if type(n) != int:
        raise TypeError("N must be a +ve Integer")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n-1)+fib(n-2)
var = int(input("NO OF FIBONACCI SERIES"))
for n in range(1,var+1):
    print(fib(n))
    

