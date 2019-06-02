#coding: utf-8
''' mbinary
#######################################################################
# File : dfs.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2019-05-27  10:02
# Description: 
    from leetcode-cn #1048: https://leetcode-cn.com/problems/longest-string-chain/
    给出一个单词列表，其中每个单词都由小写英文字母组成。

    如果我们可以在 word1 的任何地方添加一个字母使其变成 word2，那么我们认为 word1 是 word2 的前身。例如，"abc" 是 "abac" 的前身。

    词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word_1 是 word_2 的前身，word_2 是 word_3 的前身，依此类推。

    从给定单词列表 words 中选择单词组成词链，返回词链的最长可能长度。
    
#######################################################################
'''

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def isAdj(s1,s2):
            if len(s1)>len(s2):
                s1,s2 = s2,s1
            n1,n2 = len(s1),len(s2)
            if n2-n1!=1:
                return False
            i=j=0
            flag = False
            while i<n1 and j<n2:
                if s1[i]!=s2[j]:
                    if flag:
                        return False
                    flag = True
                    j+=1
                else:
                    i+=1
                    j+=1
            return True
                        
        def dfs(begin):
            ans = 1
            w = words[begin]
            n = len(w)
            if n+1 in lenDic:
                for nd in lenDic[n+1]:
                    #print(w,words[nd],isAdj(w,words[nd]))
                    if isAdj(w,words[nd]):
                        ans = max(ans,1+dfs(nd))
            return ans
        lenDic = {}
        for i in range(len(words)):
            n = len(words[i])
            if n in lenDic:
                lenDic[n].add(i)
            else:
                lenDic[n]={i}
        
        lens = sorted(lenDic)
        n = len(lens)
        ans = 0
        for i in range(n):
            if ans < n-i:
                for nd in lenDic[lens[i]]:
                    ans = max(ans,dfs(nd))          
        return ans
                
