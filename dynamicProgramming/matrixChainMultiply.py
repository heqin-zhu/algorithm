''' mbinary
#########################################################################
# File : matrixChainMultiply.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-11-05  19:09
# Description:
#########################################################################
'''
def matrixChainMultiply(seq):
    '''matrix chain multiply, find the optimalest comb to multiply
        eg ABCD,  (AB)(CD), A((BC)D)
        seq: sequence of matrix's scale, eg [A.row,A.col,B.col,C.col,D.col]
    '''
    print(seq)
    n = len(seq)-1
    mat = [[0]*n for i in range(n)]
    mark = [[0]*n for i in range(n)]
    for l in range(1,n):
        for i in range(n):
            j = i+l
            if j>=n: continue
            mat[i][j] = None
            for k in range(i,j):
                tmp = mat[i][k]+mat[k+1][j]+seq[i]*seq[k+1]*seq[j+1]
                if mat[i][j] is None or mat[i][j]>tmp:
                    mark[i][j] = k
                    mat[i][j]= tmp
    s= findSolution(mark,0,n-1)
    print(s)
    return mat[0][n-1]
def findSolution(mark,i,j):
    if j==i: return 'M{}'.format(i+1)
    if j-i==1: return 'M{} * M{}'.format(j,j+1)
    k = mark[i][j]
    return  '('+findSolution(mark,i,k)+') * ('+findSolution(mark,k+1,j)+')'

if __name__=='__main__':
    seq = [5,10,3,12,5,50,6]
    res = matrixChainMultiply(seq)
    print(res)
