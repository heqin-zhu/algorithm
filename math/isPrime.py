''' mbinary
#########################################################################
# File : isPrime.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-05-19  21:34
# Description:
#########################################################################
'''

# created by  mbinary  @2018-3-4 
# description: judge a num if it's a prime. It will be more efficient when judging many times


primes = [2,3,5,7,11,13]
def isPrime(x):
    global primes
    if x>primes[-1]:
        return genPrime(x)
    return twoDivideFind(x,primes)

def genPrime(x):
    global primes
    while x>primes[-1]:
        left = primes[-1]
        right = (left+1)**2
        lst = []
        for i in range(left,right):
            for j in primes:
                if i%j==0:break
            else:lst.append(i)
        primes+=lst
    else:return twoDivideFind(x,lst)

def twoDivideFind(x,primes):
    a,b = 0, len(primes)
    while a<=b:
        mid = (a+b)//2
        if primes[mid]<x:a=mid+1
        elif primes[mid]>x: b= mid-1
        else:return True
    return False
