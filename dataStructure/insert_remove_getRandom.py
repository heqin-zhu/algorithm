#coding: utf-8
''' mbinary
#######################################################################
# File : insert_remove_getRandom.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2019-05-24  10:01
# Description: 
    insert, remove, getRandom 的摊还时间为 O(1),
    且有重复数据, remove 一次删除一个元素
#######################################################################
'''


class RandomizedCollection:
    def __init__(self):

        self.vals = []
        self.index = {}

    def insert(self, val: int) -> bool:
        self.vals.append(val)
        if val in self.index:
            self.index[val].add(len(self.vals)-1)
            return False
        else:
            self.index[val] = {len(self.vals)-1}
            return True

    def removeAll(self, val: int) -> bool:
        if val not in self.index:
            return False
        begin = end = len(self.vals)-len(self.index[val])
        for idx in self.index.pop(val):
            if idx < begin:
                while self.vals[end] == val:
                    end += 1
                self.vals[idx] = self.vals[end]
                self.index[self.vals[idx]].remove(end)
                self.index[self.vals[idx]].add(idx)
        self.vals = self.vals[:begin]
        return True

    def remove(self, val):
        if val not in self.index:
            return False
        last = len(self.vals)-1
        idx = self.index[val].pop()
        if len(self.index[val]) == 0:
            del self.index[val]
        if idx != last:
            self.vals[idx] = self.vals[last]
            self.index[self.vals[idx]].remove(last)
            self.index[self.vals[idx]].add(idx)
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        if self.vals:
            return self.vals[random.randint(0, len(self.vals)-1)]
