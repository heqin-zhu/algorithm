''' mbinary
#########################################################################
# File : radixSort.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-07-06  15:52
# Description:
#########################################################################
'''

from random import randint
from quickSort import quickSort
from time import time


def radixSort(lst, radix=10):
    ls = [[] for i in range(radix)]
    mx = max(lst)
    weight = 1
    while mx >= weight:
        for i in lst:
            ls[(i // weight) % radix].append(i)
        weight *= radix
        lst = sum(ls, [])
        ls = [[] for i in range(radix)]
    return lst


def countSort(lst, mn, mx):
    mark = [0]*(mx-mn+1)
    for i in lst:
        mark[i-mn] += 1
    ret = []
    for n, i in enumerate(mark):
        ret += [n+mn]*i
    return ret


def timer(funcs, span, num=1000000):
    lst = [randint(0, span) for i in range(num)]
    print('range({}), {} items'.format(span, num))
    for func in funcs:
        data = lst.copy()
        t = time()
        func(data)
        t = time()-t
        print('{}: {}s'.format(func.__name__, t))


if __name__ == '__main__':
    timer([quickSort, radixSort, sorted], 1000000000000, 1000)
    timer([quickSort, radixSort, sorted], 10000, 100000)
    lst = [randint(0, 100) for i in range(1000)]
    print(countSort(lst, 0, 100) == sorted(lst))
