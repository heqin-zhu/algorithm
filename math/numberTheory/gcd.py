#coding: utf-8
''' mbinary
#######################################################################
# File : gcd.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-12-16  10:06
# Description: 
#######################################################################
'''


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return int(a*b/gcd(a, b))


def xgcd(a, b):
    '''return gcd(a,b),  x,y  where  ax+by=gcd(a,b)'''
    if b == 0:
        return a, 1, 0
    g, x, y = xgcd(b, a % b)
    return g, y, x-a//b*y


if __name__ == '__main__':
    while 1:
        a = int(input('a: '))
        b = int(input('b: '))
        print('gcd :', gcd(a, b))
        print('xgcd:', xgcd(a, b))
