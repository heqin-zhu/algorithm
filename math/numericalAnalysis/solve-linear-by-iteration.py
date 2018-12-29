''' mbinary
#########################################################################
# File : solve-linear-by-iteration.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-10-02  21:14
# Description:
#########################################################################
'''

'''
#########################################################################
# File : solve-linear-by-iteration.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.github.io
# Github: https://github.com/mbinary
# Created Time: 2018-05-04  07:42
# Description: 
#########################################################################
'''
import numpy as np 
from operator import le,lt

def jacob(A,b,x,accuracy=None,times=6):
    ''' Ax=b,  arg x is the init val, times is the time of iterating'''
    A,b,x = np.matrix(A),np.matrix(b),np.matrix(x)
    n,m = A.shape 
    if n!=m:raise Exception("Not square matrix: {A}".format(A=A))
    if b.shape !=( n,1) : raise Exception('Error: {b} must be {n} x1 in dimension'.format(b = b,n=n))
    D = np.diag(np.diag(A))
    DI = np.zeros([n,n])
    for i in range(n):DI[i,i]= 1/D[i,i]
    R = np.eye(n) - DI * A
    g = DI * b
    print('R =\n{}'.format(R))
    print('g =\n{}'.format(g))
    last = -x
    if accuracy != None:
        ct=0
        while 1:
            ct+=1
            tmp = x-last
            last = x
            mx = max ( abs(i) for i in tmp) 
            if mx<accuracy:return x
            x = R*x+g
            print('x{ct} =\n{x}'.format(ct = ct,x=x))
    else:
        for i in range(times):
            x = R*x+g
            print('x{ct} =  \n{x}'.format(ct=i+1,x=x))
    print('isLimitd: {}'.format(isLimited(A)))
    return x
def gauss_seidel(A,b,x,accuracy=None,times=6):
    ''' Ax=b,  arg x is the init val, times is the time of iterating'''
    A,b,x = np.matrix(A),np.matrix(b),np.matrix(x)
    n,m = A.shape 
    if n!=m:raise Exception("Not square matrix: {A}".format(A=A))
    if b.shape !=( n,1) : raise Exception('Error: {b} must be {n} x1 in dimension'.format(b = b,n=n))
    D =np. matrix(np.diag(np.diag(A)))
    L = np.tril(A) - D  # L = np.triu(D.T) - D
    U = np.triu(A) - D
    DLI = (D+L).I
    S = - (DLI) * U
    f = (DLI)*b
    print('S =\n{}'.format(S))
    print('f =\n{}'.format(f))
    last = -x
    if accuracy != None:
        ct=0
        while 1:
            ct+=1
            tmp = x-last
            last = x
            mx = max ( abs(i) for i in tmp) 
            if mx<accuracy:return x
            x = S*x+f
            print('x{ct} =\n{x}'.format(ct=ct,x=x))
    else:
        for i in range(times):
            x = S*x+f
            print('x{ct} =  \n{x}'.format(ct=i+1,x=x))
    print('isLimitd: {}'.format(isLimited(A)))
    return x


def isLimited(A,strict=False):
    '''通过检查A是否是[严格]对角优来判断迭代是否收敛, 即对角线上的值是否都大于对应行(或者列)的值'''
    diag = np.diag(A)
    op = lt if strict else le
    if op(A.max(axis=0),diag).all(): return True 
    if op(A.max(axis=1), diag).all(): return True 
    return False

testcase=[]
def test():
    for func,A,b,x,*args in testcase:
        acc =None 
        times = 6
        if args !=[] :
            if isinstance(args[0],int):times = args[0]
            else : acc = args[0]
        return func(A,b,x,acc,times)


if __name__ =='__main__':
    A = [[2,-1,-1],
         [1,5,-1],
         [1,1,10]
        ]
    b = [[-5],[8],[11]]
    x = [[1],[1],[1]]
    #testcase.append([gauss_seidel,A,b,x])

    A = [[2,-1,1],[3,3,9],[3,3,5]]
    b = [[-1],[0],[4]]
    x = [[0],[0],[0]]
    #testcase.append([jacob,A,b,x])

    A = [[5,-1,-1],
         [3,6,2],
         [1,-1,2]
        ]
    b=  [[16],[11],[-2]]
    x = [[1],[1],[-1]]
    testcase.append([gauss_seidel,A,b,x,0.001])
    test()
