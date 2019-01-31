#coding: utf-8
''' mbinary
#######################################################################
# File : isBipartGraph.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-12-21  15:00
# Description: Judge if a graph is bipartite
        The theorical idea is to judge whether the graph has a odd-path circle. However, it's hard to implement.
        The following codes show a method that colors the nodes by dfs.
#######################################################################
'''


def isBipartite(self, graph):
    """
    :type graph: List[List[int]]
    :rtype: bool
    """
    n = len(graph)
    self.node = graph
    self.color = {i:None for i in range(n)}
    return all(self.dfs(i,True) for i in range(n) if self.color[i] is None)
def dfs(self,n,col=True):
    if self.color[n] is None:
        self.color[n]=col
        return all(self.dfs(i,not col) for i in self.node[n])
    else:return col==self.color[n]
