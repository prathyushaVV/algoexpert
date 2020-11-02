# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 00:43:01 2020

@author: Prathyusha Vaigandla
"""

def SmallestDifferneces(arr1, arr2):
    arr1.sort()
    arr2.sort()
    left1 = 0
    left2 = 0
    diff = float("inf")
    res =[]
    smallDIff = float("inf")
    while left1 < len(arr1) and left2 < len(arr2):
        diff = abs(arr1[left1]-arr2[left2])
        if smallDIff > diff:
            smallDIff = diff
            res = [arr1[left1],arr2[left2]]
        if arr1[left1] < arr2[left2]:
            left1 += 1
        elif arr2[left2] < arr1[left1]:
            left2 += 1
        else:
            return [arr1[left1],arr2[left2]]

    return res
arr1 = [-1,5, 10, 20,28,3]
arr2 = [26, 134, 135, 15, 17]
print(SmallestDifferneces(arr1, arr2))
