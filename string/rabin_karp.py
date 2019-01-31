#coding: utf-8
''' mbinary
#########################################################################
# File : rabin_karp.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-12-11  00:01
# Description: rabin-karp algorithm
#########################################################################
'''

def isPrime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:return False
    return True
def getPrime(x):
    '''return a prime which is bigger than x'''
    for i in range(x,2*x):
        if isPrime(i):return i
def findAll(s,p):
    '''s: string   p: pattern'''
    dic={}
    n,m = len(s),len(p)
    d=0 #radix
    for c in s:
        if c not in dic:
            dic[c]=d
            d+=1
    sm = 0
    for c in p:
        if c not in dic:return []
        sm = sm*d+dic[c]

    ret = []
    cur = 0
    for i in range(m): cur=cur*d + dic[s[i]]
    if cur==sm:ret.append(0)
    tmp = n-m
    q = getPrime(m)
    cur = cur%q
    sm = sm%q
    exp = d**(m-1) % q
    for i in range(m,n):
        cur = ((cur-dic[s[i-m]]*exp)*d+dic[s[i]]) % q
        if cur == sm and p==s[i-m+1:i+1]:
            ret.append(i-m+1)
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
