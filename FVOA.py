# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:59:00 2020

@author: User
"""

def FVOAfunc(PMT,i,n):
    FVIFA=(((1+i)**n)-1)/i
    FVOA=round(PMT*FVIFA,2)
    return (FVIFA,FVOA)
PMT=int(input('請輸入每個月存入金額:'))
i=0.025
n=int(input('請輸入預計幾年後退休:'))
print('FVIFA=%.2f, FVOA=%.2f'%(FVOAfunc(PMT, i/12, n*12)))