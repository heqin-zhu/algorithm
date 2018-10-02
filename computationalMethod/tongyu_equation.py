''' mbinary
#########################################################################
# File : tongyu_equation.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-10-02  21:14
# Description:
#########################################################################
'''

# created by  mbinary  @2018-3-4 
# description: solve tongyu equation
# notice that i use -- to repr tongyu symbol

from isPrime import isPrime,primes
from operator import mul, and_
from functools import   reduce,partial
import re


def primeFactoize(x):
    '''质因数分解 , ret {p:r}'''
    if isPrime(x):return {x:1}
    mp={}
    for i in primes:
        if x==1:break
        ct=0
        while x%i==0:
            ct+=1
            x//=i
        if ct!=0:mp[i]=ct
    return mp
def xgcd(a,b):
    '''ax+by=gcd(a,b) ,用辗转相除法得到gcd,x,y'''
    def _xgcd(a,b):
        if b==0:return a,1,0
        gcd,x,y=_xgcd(b,a%b)
        return gcd,y,x-y*a//b
    if a<b:
        g,x,y = _xgcd(b,a)
        return g,y,x
    return _xgcd(a,b)

def gcd(a,b):
    return a if b==0 else gcd(b,a%b)

def lcm(a,b):
    return a*b//gcd(a,b)

def euler(x):
    mp = primeFactoize(x)
    fac = [1-1/i for i in mp]
    return round(reduce(mul,fac,x))

def  ind(m,g):
    ''' mod m ,primary root g  ->  {n:indg n}'''
    return {j:i for i in range(m-1) \
            for j in range(m) if (g**i-j)%m==0}

def gs(m,num=100):
    '''return list of  m's  primary roots below num''' 
    phi = euler(m)
    mp = primeFactoize(phi)
    checkLst = [phi//i for i in mp]
    return [i for i in range(2,num) \
            if reduce(and_,[(i**n-1)%m !=0  for n in checkLst])]

def minG(m):
    phi = euler(m)
    mp = primeFactoize(phi)
    checkLst = [phi//i for i in mp]
    i=2
    while  1:
        if reduce(and_,[(i**n-1)%m !=0  for n in checkLst]):return i
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
        return ([(sol+i*m0)%m for i in range(g)],m)
    def check(self,a,b,m):
        if m<=0:
            self.error()
            return None
        if a<0:a,b=-a,-b  ## important
        if b<0:b+= -b//m * m
        return a,b,m

    
    #def solvePoly(self,m,mp):
        ''' mod m,  mp:{index:coef}  is a dict of the polynomials' coefficient and index'''
    '''   g = minG(m)
        ind_mp = ind(m,g)
        li = []
        for i in mp:
            solve
    '''

    def solveHigh(self,a,n,b,m):
        ''' ax^n -- b (mod m)  ind_mp is a dict of  m's {n: indg n}'''
        ind_mp = ind(m,minG(m))
        tmp = ind_mp[b] - ind_mp[a]
        if tmp < 0:tmp+=m
        print(n,tmp)
        sol = self.solveLinear(n,tmp,euler(m))
        re_mp = {j:i for i ,j in ind_mp.items()}
        print(sol)
        return [re_mp[i] for i in sol[0]],m

    def solveGroup(tups):
        '''tups is a list of tongyu equation groups, like
            [(a1,b1,m1),(a2,b2,m2)...]
            and, m1,m2... are all primes
        '''
        mp = {}
        for a,b,m in tups:
            if m in mp:
                if mp[m][0]*b!=mp[m][1]*a:
                    self.noSol()
                    return
            else:mp[m] = (a,b)
        product= reduce(lambda i,j:i*j, mp.keys(), 1)
        sol = 0
        for i in mp:
            x = self.solveLinear(product//i*mp[i][0],1,i)
            sol+= x*product//i*mp[i][1]
        sol%=m
        return ([sol],m)       
    def __call__(self):
        s=input('输入同余方程，用--代表同于号，形如3--5(mod 7)代表3x模7同余于5')
        li= self.linearPat.findall(s)
        li = [(int(a),int(b),int(m)) for a,b,m in li]
        print(self.solveLinear(li[0]))


if __name__ == '__main__':
    solver  = solve()
    res = solver.solveLinear(3,6,9)
    print(res)
    print(solver.solveHigh(1,8,3,11))
