#coding: utf-8
''' mbinary
#######################################################################
# File : euler.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-12-16  10:53
# Description:
    euler function:  phi(n)
    perfect num:    \sigma (n) = 2n,     \sigma (n) is the sum of all factors of n
                    eg   \sigma (9) = 3+3+9 = 15
#######################################################################
'''
from factor import factor
from collections import Counter
from functools import reduce
from operator import mul
def phi(n):
    st  = set(factor(n))
    return round(reduce(mul,(1-1/p for p in st),n))

def sigma(n):
    ct = Counter(factor(n))
    return reduce(mul,(round((p**(ct[p]+1)-1)/(p-1)) for p in ct),1)

if __name__=='__main__':
    while 1:
        n = int(input('n: '))
        print('phi(n):',phi(n))
        print('sigma(n):',sigma(n))

