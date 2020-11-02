# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 23:39:55 2020

@author: Prathyusha Vaigandla
"""
array = [9, 10, 11, 0, -4 ,-5, -6, -1]
count = 0
target = 0
triplets = []
array.sort()
for i in range(len(array)-3):
    for j in range(i+1,len(array)-2):
        left = j+1
        right = len(array)-1
        while left<right:
            cn = array[i]+array[j]+array[left]+array[right]
            if cn == target:
                triplets.append([array[i],array[j],array[left],array[right]])
                left += 1
                right -= 1
                count += 1
            elif cn<target:
                left += 1
            elif cn > target:
                right -= 1
    
print(count)
print(triplets)