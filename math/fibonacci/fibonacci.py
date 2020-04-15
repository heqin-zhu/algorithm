#coding: utf-8
''' mbinary
#######################################################################
# File : fibonacci.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.github.io
# Github: https://github.com/mbinary
# Created Time: 2019-02-03  19:10
# Description: use matrix and fast pow to calculate big numbr fibonacci value.
#######################################################################
'''


def fib(n):
    """Calculates the nth Fibonacci number"""
    mat, p = (1, 1, 1, 0), n-2
    if n <= 0:  # for negative fib item,  use f(n) = f(n+2)-f(n-1) to calculate
        mat = (0, 1, 1, -1), 2-n
    li = matrix_pow((0, 1, 1, -1), 1-n)
    return li[0]+li[1]


def matrix_pow(mat, n):
    ans = (1, 0, 0, 1)  # element matrix
    while n > 0:
        if n % 2 == 1:
            ans = matrix_mul(ans, mat)
        n >>= 1
        mat = matrix_mul(mat, mat)
    return ans


def matrix_mul(a, b):
    '''a,b are four-item tuple, represent matrix [[a[0],a[1]],[a[2],a[3]]]'''
    return a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3], a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3]


if __name__ == '__main__':
    for i in range(-5, 5):
        print(i, fib(i))
