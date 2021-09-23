# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 18:21:02 2021

@author: andop
"""

for n in range(5,21): 
    print(n)
    count = 0
    while n > 1:
        
       
       if n%2 != 0:
           n = 3*n + 1
       else:
           n = n/2
           count += 1
    
    print(count)