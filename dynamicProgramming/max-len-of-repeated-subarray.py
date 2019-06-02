#coding: utf-8
''' mbinary
#######################################################################
# File : max-len-of-repeated-subarray.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2019-05-27  08:25
# Description: 
    给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
#######################################################################
'''
def findLength(A,B):
    n,m = len(A),len(B)
    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if A[i-1]==B[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
    return max(max(row) for row in dp)
