#coding: utf-8
''' mbinary
#######################################################################
# File : maxXor.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-12-22  09:51
# Description:
    maximum_xor_of_two_numbers_in_an_array:
        using  trie data structure
        O(k*n) where n=length(array),k  is the max length of radix of num
#######################################################################
'''

class node:
    def __init__(self,key,hasKey = False):
        self.key = key
        self.hasKey = hasKey
        self.children={}
    def __getitem__(self,key):
        return self.children[key]
    def __len__(self):
        return len(self.children)
    def __setitem__(self,key,val):
        self.children[key]=val
    def __contains__(self,key):
        return key in self.children
class trie:
    def __init__(self,maxDepth=32):
        self.root=node(None)
        self.maxDepth = maxDepth
    def add(self,num):
        nd = self.root
        s = bin(num)[2:].rjust(self.maxDepth,'0')
        for n in s:
            if n not in nd:
                nd[n]=node(n)
            nd=nd[n]
    def search(self,num):
        ret = 0
        nd = self.root
        s = bin(num)[2:].rjust(self.maxDepth,'0')
        for n in s:
            # note that it's the flip bit
            flip = '1' if n=='0' else '0'
            if flip in nd:
                ret=ret*2+1
                nd=nd[flip]
            else:
                ret*=2
                nd=nd[n]
        return ret

def findMaximumXOR(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:return 0
    n = len(bin(max(nums)))-1
    t = trie(n)
    for i  in nums:t.add(i)
    return max(t.search(i) for i in nums)

if __name__=='__main__':
    from random import randint
    nums  = [randint(1,int(1e18)) for i in 100]
    findMaximumXOR(nums)
