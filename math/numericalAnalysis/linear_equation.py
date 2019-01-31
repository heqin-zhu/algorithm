''' mbinary
#########################################################################
# File : linear_equation.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-10-02  21:14
# Description:
#########################################################################
'''

#coding: utf-8
'''************************************************************************
    > File Name: doolittle.py
    > Author: mbinary
    > Mail: zhuheqin1@gmail.com 
    > Blog: https://mbinary.xyz
    > Created Time: 2018-04-20  08:32
 ************************************************************************'''

import  numpy as np
def getLU(A):
    '''doolittle :     A = LU, 
        L is in  down-triangle form, 
        U is in  up-triangle form
    '''
    m,n = A.shape
    if m!=n:raise Exception("this matrix is not inversable")

    L = np.zeros([m,m])
    U = np.zeros([m,m])
    L = np.matrix(L)
    U = np. matrix(U)
    U[0] = A[0]
    L[:,0] = A[:,0] / A[0,0]
    for i in range(1,m):
        for j in range(i,m):
            U[i,j]= A[i,j] - sum(L[i,k]*U[k,j] for k in range(i))
            L[j,i] = (A[j,i] - sum(L[j,k]*U[k,i] for k in range(i)))/U[i,i]
    print(L)
    print(U)
    return L,U


def gauss_prior_elimination(A):
    '''using guass elimination,get up_trianglge form of A'''
    m,n = A.shape
    if m!=n:raise Exception("[Error]: matrix is not inversable")
    B = np.matrix(A,dtype=float) # necessary,otherwise when the dtype of A is int, then it will be wrong
    for  i in range(m-1):
        col = abs(B[i:,i]) #  note using abs value,  return a matrix in (m-i)x1 form
        mx = col.max()
        if mx==0: raise Exception("[Error]: matrix is not inversable")
        pos = i+col.argmax()
        if pos != i :  B[[pos,i],:] = B[[i,pos],:]  #  note how to swap cols/rows
        B[i,:] = 1/mx*B[i,:]
        for j in range(i+1,m):
            #print(B)
            B[j,:] -= B[j,i] * B[i,:]
    print(B)
    return B

def solveDown(A,b):
    '''A is a matrix in down-triangle form'''
    sol = np.zeros(b.shape)
    for i in range(b.shape[0]):
        sol[i,0] = (b[i,0]-sum(A[i,j]*sol[j,0] for j in range(i)))/A[i,i]
    return sol

def solveUp(A,b):
    '''A is a matrix in up-triangle form'''
    sol = np.zeros(b.shape)
    n = b.shape[0]
    for i in range(n-1,-1,-1):
        sol[i,0] = (b[i,0]-sum(A[i,j]*sol[j,0] for j in range(n-1,i,-1)))/A[i,i]
    return sol
def doolittle(A,b):
    L,U = getLU(A)
    y = solveDown(L,b)
    x = solveUp(U,y)
    print(y)
    print(x)
    return x
def ldlt(A,b):
    L,U = getLU(A)
    D = np.diag(np.diag(U))
    print(D,"D")
    z = np.linalg.solve(L,b)
    print(z,"z")
    y = np.linalg.solve(D,z)
    print(y,"y")
    x = np.linalg.solve(L.T,y)
    print(x,"x")
    return x
if __name__ == '__main__':
    A = np.matrix([[10,5,0,0],
                     [2,2,1,0],
                     [0,10,0,5],
                      [0,0,2,1]])
    b = np.matrix([[5],[3],[27],[6]])
    gauss_prior_elimination(A)

    '''ldlt
    A = np.matrix([[-6,3,2],
                     [3,5,1],
                     [2,1,6]])
    b = np.matrix([[-4],[11],[-8]])
    ldlt(A,b)
    '''
'''
    A = np.matrix([[2,1,1],
                     [1,3,2],
                     [1,2,2]])
    b = np.matrix([[4],[6],[5]])
    doolittle(A,b)
'''
    
