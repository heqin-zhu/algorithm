#coding: utf-8
''' mbinary
#######################################################################
# File : unionFind.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-12-18  14:53
# Description: 
    班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

    给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果 M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
#######################################################################
'''


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        self.data = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if M[i][j]==1:
                    self.union(i,j)
        ret = set()
        for i in range(n):
            ret.add(self.find(i))
        return len(ret)
    def find(self,i):
        if self.data[i]!=i:
            self.data[i] = self.find(self.data[i])
        return self.data[i]
    def union(self,i,j):
        if i!=j:
            n = self.find(i)
            if n!=self.find(j):
                self.data[n]= self.data[j]  
