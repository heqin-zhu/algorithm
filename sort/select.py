''' mbinary
#########################################################################
# File : select.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-07-06  17:13
# Description:
#########################################################################
'''

from random import randint


def select(lst, i):
    lst = lst.copy()

    def partition(a, b):
        pivot = lst[a]
        while a < b:
            while a < b and lst[b] > pivot:
                b -= 1
            if a < b:
                lst[a] = lst[b]
                a += 1
            while a < b and lst[a] < pivot:
                a += 1
            if a < b:
                lst[b] = lst[a]
                b -= 1
        lst[a] = pivot
        return a

    def _select(a, b):
        if a >= b:
            return lst[a]
        # randomized select
        n = randint(a, b)
        lst[a], lst[n] = lst[n], lst[a]
        pos = partition(a, b)
        if pos > i:
            return _select(a, pos-1)
        elif pos < i:
            return _select(pos+1, b)
        else:
            return lst[pos]
    return _select(0, len(lst)-1)


if __name__ == '__main__':
    lst = [randint(0, 1000) for i in range(100)]
    st = sorted(lst)
    for i in range(10):
        n = randint(0, 99)
        print('select {}th: \nexpect: {}\ngot: {}'.format(
            n, st[n], select(lst, n)))
