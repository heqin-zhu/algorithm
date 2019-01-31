#coding: utf-8
''' mbinary
#######################################################################
# File : fastPow.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-12-17  21:39
# Description: fast power
#######################################################################
'''

def fastPow(a,n):
    '''a^n'''
    rst = 1
    while n:
        if n%2:
            rst *=a
        n>>=1
        a*=a
    return rst

def fastMul(a,b):
    '''a*b'''
    rst = 0
    while b:
        if b&1:
            rst +=a
        b>>=1
        a*=2
