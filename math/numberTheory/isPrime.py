''' mbinary
#########################################################################
# File : isPrime.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-03-04  21:34
# Description:
#########################################################################
'''
from random import randint


def quickMulMod(a,b,m):
    '''a*b%m,  quick'''
    ret = 0
    while b:
        if b&1:
            ret = (a+ret)%m
        b//=2
        a = (a+a)%m
    return ret

def quickPowMod(a,b,m):
    '''a^b %m, quick,  O(logn)'''
    ret =1
    while b:
        if b&1:
            ret =quickMulMod(ret,a,m)
        b//=2
        a = quickMulMod(a,a,m)
    return ret


def isPrime(n,t=5):
    '''miller rabin primality test,  a probability result
        t is the number of iteration(witness)
    '''
    t = min(n-3,t)
    if n<2:
        print('[Error]: {} can\'t be classed with prime or composite'.format(n))
        return
    if n==2: return True
    d = n-1
    r = 0
    while d%2==0:
        r+=1
        d//=2
    tested=set()
    for i in range(t):
        a = randint(2,n-2)
        while a in tested:
            a = randint(2,n-2)
        tested.add(a)
        x= quickPowMod(a,d,n)
        if x==1 or x==n-1: continue  #success, 
        for j in range(r-1):
            x= quickMulMod(x,x,n)
            if x==n-1:break
        else:
            return False
    return True

'''
we shouldn't use Fermat's little theory
Namyly:
    For a prime p, and any number a where (a,n)=1
    a ^(p-1)  \equiv  1 (mod p)

The inverse theorem of it is not True.

a counter-example:  2^340  \equiv 1 (mod 341), but 341 is a composite
'''

class primeSieve:
    '''sieve of Eratosthenes, It will be more efficient when judging many times'''
    primes = [2,3,5,7,11,13]
    def isPrime(self,x):
        if x<=primes[-1]:
            return twoDivideFind(x,self.primes)
        while x>self.primes[-1]:
            left = self.primes[-1]
            right = (left+1)**2
            lst = []
            for i in range(left,right):
                for j in self.primes:
                    if i%j==0:break
                else:lst.append(i)
            self.primes+=lst
        return twoDivideFind(x,lst)

def twoDivideFind(x,li):
    a,b = 0, len(li)
    while a<=b:
        mid = (a+b)//2
        if li[mid]<x:a=mid+1
        elif li[mid]>x: b= mid-1
        else:return mid
    return -1

if __name__=='__main__':
    n = 100
    print('prime numbers below',n)
    print([i for i in range(n) if isPrime(i)])
    while 1:
        n = int(input('n: '))
        print(isPrime(n))
