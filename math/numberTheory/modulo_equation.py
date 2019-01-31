''' mbinary
#########################################################################
# File : modulo_equation.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-3-4  21:14
# Description:
   `--` represents modulo symbol
#########################################################################
'''

import re

from gcd import xgcd
from euler import phi
from isPrime import isPrime
from factor import factor

def  ind(m,g):
    ''' mod m ,primary root g  ->  {n:indg n}'''
    return {j:i for i in range(m-1) \
            for j in range(m) if (g**i-j)%m==0}

def gs(m,num=100):
    '''return list of  m's  primary roots below num''' 
    p = phi(m)
    mp = factor(p)
    checkLst = [p//i for i in mp]
    return [i for i in range(2,num) if all((i**n-1)%m !=0  for n in checkLst)]

def minG(m):
    p = phi(m)
    mp = factor(p)
    checkLst = [p//i for i in mp]
    i=2
    while  1:
        if all((i**n-1)%m !=0  for n in checkLst):return i
        i+=1

class solve:
    def __init__(self,equ=None):
        self.linearPat= re.compile(r'\s*(\d+)\s*--\s*(\d+)[\s\(]*mod\s*(\d+)')
        self.sol  = []
        #self.m = m
        #self.ind_mp = ind(m,minG(m))
    def noSol(self):
        print('equation {equ} has no solution'.format(equ=self.equ))
    def error(self):
        print("Error! The divisor m must be postive integer")
    def solveLinear(self,a,b,m):
        '''ax--b(mod m): solve linear equation with one unknown
            return  ([x1,x2,...],m)
        '''
        a,b,m = self.check(a,b,m)
        g,x,y=xgcd(a,m)
        if a*b%g!=0:
            self.noSol()
            return None
        sol=x*b//g
        m0 = m//g
        sols = [(sol+i*m0)%m for i in range(g)]
        print('{}x--{}(mod {}), solution: {} mod {}'.format(a,b,m,sols,m))
        return (sols,m)
    def check(self,a,b,m):
        if m<=0:
            self.error()
            return None
        if a<0:a,b=-a,-b  ## important
        if b<0:b+= -b//m * m
        return a,b,m

    def solveHigh(self,a,n,b,m):
        ''' ax^n -- b (mod m)  ind_mp is a dict of  m's {n: indg n}'''
        ind_mp = ind(m,minG(m))
        tmp = ind_mp[b] - ind_mp[a]
        if tmp < 0:tmp+=m
        sol = self.solveLinear(n,tmp,phi(m))
        re_mp = {j:i for i ,j in ind_mp.items()}
        sols = [re_mp[i] for i in sol[0]]
        print('{}x^{}--{}(mod {}),  solution: {} mod {}'.format(a,n,b,m,sols,m))
        return sols,m

    def solveGroup(self,tups):
        '''tups is a list of tongyu equation groups, like
            [(a1,b1,m1),(a2,b2,m2)...]
            and, m1,m2... are all primes
        '''
        mp = {}
        print('solving group of equations: ')
        for a,b,m in tups:
            print('{}x--{}(mod {})'.format(a,b,m))
            if m in mp:
                if mp[m][0]*b!=mp[m][1]*a:
                    self.noSol()
                    return
            else:mp[m] = (a,b)
        product = 1
        for i in mp.keys():
            product *=i
        sol = [0]
        for i in mp:
            xs,m = self.solveLinear(product//i*mp[i][0],1,i)
            new = []
            for x in xs:
                cur = x*product//i*mp[i][1]
                for old in sol:
                    new.append(old+cur)
            sol = new
        sol= [i%product for i in sol]
        print('final solution: {} mod {}'.format(sol,product))
        return sol,product
    def __call__(self):
        s=input('输入同余方程，用--代表同于号，形如3--5(mod 7)代表3x模7同余于5')
        li= self.linearPat.findall(s)
        li = [(int(a),int(b),int(m)) for a,b,m in li]
        print(self.solveLinear(li[0]))


if __name__ == '__main__':
    solver  = solve()
    res = solver.solveLinear(3,6,9)
    print()
    res = solver.solveHigh(1,8,3,11)
    print()
    res = solver.solveGroup([(5,11,2),(3,8,5),(4,1,7)])
