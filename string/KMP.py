#coding: utf-8
''' mbinary
#########################################################################
# File : KMP.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-12-11  14:02
# Description:
#########################################################################
'''

def getPrefixFunc(s):
    '''return the list of prefix function of s'''
    length = 0
    i = 1
    n = len(s)
    ret = [0]
    while i<n:
        if s[i]==s[length]:
            length +=1
            ret.append(length)
            i+=1
        else:
            if length==0:
                ret.append(0)
                i+=1
            else:
                length = ret[length-1]
    return ret

def findAll(s,p):
    pre = getPrefixFunc(p)
    i = j  =0
    n,m = len(s),len(p)
    ret = []
    while i<n:
        if s[i]==p[j]:
            i+=1
            j+=1
            if j==m:
                ret.append(i-j)
                j=pre[j-1]
        else:
            if j==0: i+=1
            else: j = pre[j-1]
    return ret
def randStr(n=3):
    return [randint(ord('a'),ord('z')) for i in range(n)]

if __name__ =='__main__':
    from random import randint
    s = randStr(50)
    p = randStr(1)
    print(s)
    print(p)
    print(findAll(s,p))
