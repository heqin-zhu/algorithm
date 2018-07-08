from functools import total_ordering

@total_ordering
class node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.frequency = 1
        self.left=left
        self.right=right
    def __lt__(self,x):
        return self.val<x.val
    def __eq__(self,x):
        return self.val==x.val
    def inc(self):
        self.val+=1
    def dec(self):
        self.val-=1
    def incFreq(self):
        self.frequency +=1
    def decFreq(self):
        self.frequency -=1

class binaryTree:
    def __init__(self,reverse = True):
        self.reverse = reverse
        self.data=None
    def cmp(self,n1,n2):
        ret=0
        if n1 < n2: ret=-1
        if n1 > n2: ret= 1
        return ret * -1 if self.reverse else ret
    def addNode(self,nd):
        def _add(prt,chd):
            if self.cmp(prt,chd)==0:
                prt.incFreq()
                return
            if self.cmp(prt,chd)<0:

        if not isinstance(nd,node):nd=node(nd)
        if not self.root :
            self.root=node(val)
        else:
            if self.root == val:
                self.root.incfreq()
            else:
                cur = self.root
    def build(self,lst):
        dic = {}
        for i in lst:
            if i in dic:
                dic[i].incFreq()
            else:
                dic[i] = node(i)
        self.data =list( dic.values())

        
