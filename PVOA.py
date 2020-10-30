# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:12:52 2020

@author: User
"""

def PVOAfunc(PMT,i,n):
    pvoa=PMT*((1-((1+i)**-n))/i)
    return pvoa
cost=int(input('請輸入基金購買金額:'))
PMT=int(input('請輸入每年可領金額:'))
i=(int(input('請輸入年利率:')))/100
n=int(input('請輸入可領取年數:'))
res=PVOAfunc(PMT, i, n)
diff=res-cost
if diff<=0:
    print('教育基金現值為:%.2f，淨賺金額為%.2f，不適合購入。'%(res,diff))
else:
    print('教育基金現值為:%.2f，淨賺金額為%.2f，適合購入。'%(res,diff))
