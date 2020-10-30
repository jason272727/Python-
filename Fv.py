# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:46:31 2020

@author: User
"""

def func10(pv,i,n):
    fv=pv*((1+i)**n)
    return fv
pv=100
i=0.03
n=int(input('請輸入期數:'))
fv=func10(pv,i,n)
print('%d年後的終值為:%.2f'%(n,fv))