#coding: utf-8
''' mbinary
#######################################################################
# File : min-window-substring.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2019-05-26  21:39
# Description:
from leetcode-cn #76: https://leetcode-cn.com/problems/minimum-window-substring/

    给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：
    如果 S 中不存这样的子串，则返回空字符串 ""。
    如果 S 中存在这样的子串，我们保证它是唯一的答案。

since you have to find the minimum window in S which has all the characters from T, you need to expand and contract the window using the two pointers and keep checking the window for all the characters. This approach is also called Sliding Window Approach.

L ------------------------ R , Suppose this is the window that contains all characters of T
        L----------------- R , this is the contracted window. We found a smaller window that still contains all the characters in T

When the window is no longer valid, start expanding again using the right pointer.
#######################################################################
'''

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def expand(j,lacked,dic):
            while j<n and lacked:
                if s[j] in lacked:
                    lacked[s[j]]-=1
                    if lacked[s[j]]==0:
                        del lacked[s[j]]
                dic[s[j]]+=1
                j+=1
            return j
        def contract(left,right):
            for i in range(left,right):
                dic[s[i]]-=1
                if dic[s[i]]==0:
                    del dic[s[i]]
                if s[i] in chars and (s[i] not in dic or dic[s[i]]<chars[s[i]]):
                    return i+1,{s[i]:1}
        n ,i, j= len(s),0,0
        ans = ''
        dic,lacked = defaultdict(int), defaultdict(int)
        for c in t:
            lacked[c]+=1
        chars = lacked.copy()
        while j<n and lacked:
            j = expand(j,lacked,dic)
            if  not lacked:
                i,lacked=contract(i,j)
                if ans=='' or len(ans)>j-i+1:
                    ans = s[i-1:j]
        return ans 
