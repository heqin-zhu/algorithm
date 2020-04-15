#coding: utf-8
''' mbinary
#######################################################################
# File : hammingDistance.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-12-17  17:36
# Description:
    hamming distance is the number of different position (or binary bit for number) of two strings.
    eg   'abac', 'ab': 2            1010,11 : 3
#######################################################################
'''


def hammingDistance(a, b):
    if isinstance(a, int):
        n = a ^ b
        ct = 0
        while n:
            ct += n % 2
            n >>= 1
        return ct
    else:
        n, m = len(a), len(b)
        ret = 0
        for i, j in zip(a, b):
            ret += i == j
        return ret+abs(n-m)


def totalHammingDistance(lst):
    '''return sum of any two items(num or lst( str)) in lst'''
    length = len(lst)
    if length == 0:
        return 0
    if isinstance(lst[0], int):
        bits = [0] * len(bin(max(lst)))
        for n in lst:
            ct = 0
            while n:
                if n % 2 == 1:
                    bits[ct] += 1
                ct += 1
                n >>= 1
        return sum(i*(length-i) for i in bits)
    else:
        mx = len(max(lst, key=len))
        position = [dict() for i in range(mx)]
        for li in lst:
            for i, x in enumerate(li):
                if x in position[i]:
                    position[i][x] += 1
                else:
                    position[i][x] = 1
        ret = 0
        for dic in position:
            left = length
            for i in dic.values():
                ret += i*(left-i)  # key step
                left -= i        # key step
        return ret
