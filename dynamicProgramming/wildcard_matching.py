#coding: utf-8
''' mbinary
#######################################################################
# File : wildcard_matching.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-12-13  22:46
# Description: 
    wild card   '*'  matches 0 or any chars, and '?' matches any single char.
#######################################################################
'''


'''
idea

dynamic programming

dp[m+1][n+1]:  bool

i:n,  j:m
dp[j][i] indicates if s[:i+1] matches p[:j+1]

initial: dp[0][0] = True, dp[0][i],dp[j][0] = False
only if p startswith '*',  dp[1][0] = True.

if   p[j] = '*': dp[j][i] = dp[j-1][i] or dp[j][i-1]
elif p[j] = '?': dp[j][i] = dp[j-1][i-1]
else           : dp[j][i] = dp[j-1][i-1] and s[i] == p[j]
'''

# leetcode: q44 https://leetcode.com/problems/wildcard-matching/description/

def isMatch(self, s, p):
    """
    :type s: str
    :type p: str   pattern str including wildcard
    :rtype: bool
    """
    n,m = len(s),len(p)
    last =  [False]*(n+1)
    last[0] = True
    for j in range(m):
        if p[j]=='*':
            for i in range(n):
                last[i+1] = last[i+1] or last[i]
        elif p[j]=='?':
            last.pop()
            last.insert(0,False)
        else:
            li = [False]
            for i in range(n):
                li.append( last[i] and p[j]==s[i])
            last = li
    return last[-1]
