# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 00:16:02 2020

@author: User
"""

def PMTfunc(PV,r,n):
    pmt=PV*((r*((1+r)**n))/(((1+r)**n)-1))
    return pmt
PV=int(input('請輸入貸款金額:'))
r=(int(input('請輸入年利率:')))/100
n=int(input('請輸入欲償還年限:'))
print('每年須還:%.2f'%(PMTfunc(PV,r,n)))