''' mbinary
#########################################################################
# File : bloomFilter.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-10-17  11:19
# Description:
#########################################################################
'''
from bitarray import bitarray

import mmh3

class bloomFilter(set):
    def __init__(self,size,hash_count):
        super(bloomFilter,self).__init__()
        self.bits = bitarray(size)
        self.bits.setall(0)
        self.size = size
        self.hash_count = hash_count
    def __len__(self):
        return self.size
    def __iter__(self):
        return iter(self.bits)
    def add(self,item):
        for i in range(self.hash_count):
            idx = mmh3.hash(item,i) % self.size
            self.bits[idx]=1
        return self
    def __contains__(self,item):
        idxs =  [mmh3.hash(item,i)%self.size for i in range(self.hash_count)]
        return all([self.bits[i]==1 for i in idxs])
