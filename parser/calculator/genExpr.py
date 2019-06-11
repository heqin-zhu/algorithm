''' mbinary
#########################################################################
# File : genExpr.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2019-04-16  09:41
# Description:
#########################################################################
'''
from random import randint


def genOp(li):
    return li[randint(0, len(li)-1)]


def genNum(n=20):
    return randint(1, n)


def genFactor(n=3):
    n = randint(1, n)
    ret = [str(genNum())]
    for i in range(n):
        ret.append(genOp('*/'))
        ret.append(str(genNum()))
    return ''.join(ret)


def genExpr(n=8):
    n = randint(3, n)
    ret = [genFactor()]
    for i in range(n):
        ret.append(genOp('+-'))
        ret.append(genFactor())
    return ' '.join(ret)


if __name__ == '__main__':
    s = genExpr()
    print('evaluate "{}" == {}'.format(s, eval(s)))
