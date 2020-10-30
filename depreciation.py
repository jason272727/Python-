# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 01:23:52 2020

@author: User
"""

def func1(c,sa,y):
    return (c-sa)/y
def func2(y,d,ba):
    ad=0
    for i in range(1,y+1):
        yearcounter=i
        ad=ad+d
        bv=ba-ad
        print('%2d%12d%12d%12d'%(yearcounter,d,ad,bv))
cost=100000
salvage=10000
year=10
print('%2s%8s%8s%8s'%('年度','每年折舊','累計折舊','期末帳面價值'))
depreciation=func1(cost,salvage,year)
res=func2(year, depreciation, cost)