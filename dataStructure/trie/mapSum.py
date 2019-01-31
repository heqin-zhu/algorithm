#coding: utf-8
''' mbinary
#######################################################################
# File : mapSum.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-12-14  23:11
# Description: 
    实现一个 MapSum 类里的两个方法，insert 和 sum。

    对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值。如果键已经存在，那么原来的键值对将被替代成新的键值对。

    对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。

    示例 1:

        输入: insert("apple", 3), 输出: Null
        输入: sum("ap"), 输出: 3
        输入: insert("app", 2), 输出: Null
        输入: sum("ap"), 输出: 5
        leetcode-ch:677 https://leetcode-cn.com/problems/map-sum-pairs/
#######################################################################
'''

class node:
    def __init__(self,ch,n=0):
        self.ch = ch
        self.n = n
        self.children={}
    def __getitem__(self,ch):
        return self.children[ch]
    def __setitem__(self,ch,nd):
        self.children[ch]=nd
    def __len__(self):
        return len(self.children)
    def __iter__(self):
        return iter(self.children.values())
    def __delitem(self,ch):
        del self.children[ch]
    def __contains__(self,ch):
        return ch in self.children
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = node('')

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        nd = self.root
        for i in key:
            if i not in nd:
                nd[i] = node(i)
            nd = nd[i]
        nd.n = val
    def visit(self,nd):
        ret = nd.n
        for chd in nd:
            ret+=self.visit(chd)
        return ret
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        nd = self.root
        for ch in prefix:
            if ch in nd:
                nd = nd[ch]
            else:return 0
        return self.visit(nd)

