#coding: utf-8
''' mbinary
#######################################################################
# File : factorize.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-12-16  09:36
# Description: factorization, using pollard's rho algorithm and miller-rabin primality test
#######################################################################
'''

from random import randint
from isPrime import isPrime
from gcd     import gcd

def factor(n):
    '''pollard's rho algorithm'''
    if n<1:raise Exception('[Error]: {} is less than 1'.format(n))
    if n==1: return []
    if isPrime(n):return [n]
    fact=1
    cycle_size=2
    x = x_fixed = 2
    c = randint(1,n)
    while fact==1:
        for i in range(cycle_size):
            if fact>1:break
            x=(x*x+c)%n
            if x==x_fixed:
                c = randint(1,n)
                continue
            fact = gcd(x-x_fixed,n)
        cycle_size *=2
        x_fixed = x
    return factor(fact)+factor(n//fact)


if __name__=='__main__':
    while 1:
        n = int(input('n: '))
        print(factor(n))
