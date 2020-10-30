# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:23:40 2020

@author: User
"""

def pvfunc(fv,r,n):
    pv=fv/((1+r)**n)
    return pv
fv=float(input('請輸入終值:'))
r=(float(input('請輸入年利率:')))/100
n=int(input('請輸入期數:'))
print('%d年後現值為%.2f'%(n,pvfunc(fv, r, n)))