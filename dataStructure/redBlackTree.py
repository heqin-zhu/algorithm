'''
#########################################################################
# File : redBlackTree.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-07-12  20:34
# Description: 
#########################################################################
'''
from functools import total_ordering
from random import randint, shuffle

@total_ordering
class node:
    def __init__(self,val,left=None,right=None,isBlack=False):
        self.val =val
        self.left = left
        self.right = right
        self.isBlack  = isBlack
    def __lt__(self,nd):
        return self.val < nd.val
    def __eq__(self,nd):
        return nd is not None and self.val==nd.val
    def setChild(self,nd,isLeft = True):
        if isLeft: self.left = nd
        else: self.right = nd
    def getChild(self,isLeft):
        if isLeft: return self.left
        else: return self.right
    def __bool__(self):
        return self.val is not None
    def __str__(self):
        color = 'B' if self.isBlack else 'R'
        return f'{color}-{self.val:}'
    def __repr__(self):
        return f'node({self.val},isBlack={self.isBlack})'
class redBlackTree:
    def __init__(self):
        self.root = None
    def getParent(self,val):
        if isinstance(val,node):val = val.val
        if self.root.val == val:return None
        nd = self.root
        while nd:
            if nd.val>val and  nd.left is not None:
                if nd.left.val == val: return nd
                else: nd = nd.left
            elif nd.val<val and  nd.right is not None:
                if nd.right.val == val: return nd
                else: nd = nd.right
    def find(self,val):
        if isinstance(val,node):val = val.val
        nd = self.root
        while nd:
            if nd.val ==val:
                return nd
            elif nd.val>val:
                nd = nd.left
            else:
                nd = nd.right
    @staticmethod
    def checkBlack(nd):
        return nd is None or nd.isBlack
    @staticmethod
    def setBlack(nd,isBlack):
        if nd is not None:
            if isBlack is None or isBlack:
                nd.isBlack = True
            else:nd.isBlack = False
    def insert(self,val):
        if isinstance(val,node):val = val.val
        def _insert(root,nd):
            '''return parent''' 
            while root:
                if root == nd:return None
                elif root>nd:
                    if root.left :
                        root=root.left
                    else:
                        root.left = nd
                        return root
                else:
                    if root.right:
                        root = root.right
                    else:
                        root.right = nd
                        return root
        # insert part
        nd = node(val)
        if self.root is None:
            self.root = nd
            self.setBlack(self.root,True)
            return
        parent = _insert(self.root,nd)
        if parent is None: return
        if not parent.isBlack: self.fixUpInsert(parent,nd)

    def fixUpInsert(self,parent,nd):
        ''' adjust color and level,  there are two red nodes: the new one and its parent'''
        while not self.checkBlack(parent):
            grand = self.getParent(parent)
            isLeftPrt = grand.left == parent 
            uncle = grand.getChild(not isLeftPrt)
            if not self.checkBlack(uncle):
                # case 1:  new node's uncle is red
                self.setBlack(grand, False)
                self.setBlack(grand.left, True)
                self.setBlack(grand.right, True)
                nd = grand
                parent = self.getParent(nd)
            else:
                # case 2: new node's uncle is black(including nil leaf)
                isLeftNode = parent.left==nd
                if isLeftNode ^ isLeftPrt:
                    # case 2.1 the new node is inserted in left-right or right-left form
                    #         grand               grand
                    #     parent        or            parent
                    #          nd                   nd
                    parent.setChild(nd.getChild(isLeftPrt),not isLeftPrt)
                    nd.setChild(parent,isLeftPrt)
                    grand.setChild(nd,isLeftPrt)
                    nd,parent = parent,nd
                # case 2.2 the new node is inserted in left-left or right-right form
                #         grand               grand
                #      parent        or            parent
                #     nd                                nd
                grand.setChild(parent.getChild(not isLeftPrt),isLeftPrt)
                parent.setChild(grand,not isLeftPrt)
                self.setBlack(grand, False)
                self.setBlack(parent, True)
        self.setBlack(self.root,True)
    def sort(self,reverse = False):
        ''' return a generator of sorted data'''
        def inOrder(root):
            if root is None:return
            if reverse:
                yield from inOrder(root.right)
            else:
                yield from inOrder(root.left)
            yield root
            if reverse:
                yield from inOrder(root.left)
            else:
                yield from inOrder(root.right)
        yield from inOrder(self.root)
    def getSuccessor(self,val):
        if isinstance(val,node):val = val.val
        def _inOrder(root):
            if root is None:return
            if root.val>= val:yield from _inOrder(root.left)
            yield root
            yield from _inOrder(root.right)
        gen = _inOrder(self.root)
        for i in gen:
            if i.val==val:
                try: return gen.__next__()
                except:return None

    def delete(self,val):
        # delete node in a binary search tree
        if isinstance(val,node):val = val.val
        nd = self.find(val)
        if nd is None: return
        y = None
        if nd.left and nd.right:
            y= self.getSuccessor(val)
        else:
            y = nd
        py = self.getParent(y.val)
        x = y.left if y.left else y.right
        if py is None:
            self.root = x
        elif y==py.left:
            py.left = x
        else:
            py.right = x
        if y != nd:
            nd.val = y.val

        # adjust colors and rotate
        if self.checkBlack(y): self.fixUpDel(py,x)

    def fixUpDel(self,prt,chd):
        if self.root == chd or not self.checkBlack(chd):
            self.setBlack(chd, True)
            return
        isLeft = prt.left == chd 
        brother = prt.getChild(not isLeft)
        if self.checkBlack(brother):
            # case 1: brother is black
            lb = self.checkBlack(brother.left)
            rb = self.checkBlack(brother.right)
            if lb and rb: 
                # case 1.1: brother is black and two kids are black
                self.setBlack(brother,False)
                chd = prt
            elif lb or rb:
                # case 1.2: brother is black and two kids's colors differ
                if self.checkBlack(brother.getChild(not isLeft)):
                    # uncle's son is nephew, and niece for uncle's daughter
                    nephew = brother.getChild(isLeft),
                    print(nephew)
                    self.setBlack(nephew,True)
                    self.setBlack(brother,False)

                    # brother right rotate
                    prt.setChild(nephew,not isLeft)
                    nephew.setChild(brother, not isLeft)
                    brother = prt.right

                # case 1.3: brother is black and two kids are red
                brother.isBlack = prt.isBlack
                self.setBlack(prt,True)
                self.setBlack(brother.right,True)

                # prt left rotate
                prt.setChild(brother.getChild(isLeft),not isLeft)
                brother.setChild(prt,isLeft)
                chd = self.root


        else:
            # case 2: brother is red
            prt.setChild(brother.getChild(isLeft), not isLeft)
            brother.setChild(prt, isLeft)
            self.setBlack(prt,False)
            self.setBlack(brother,True)
        self.setBlack(chd,True)

    def display(self):
        def getHeight(nd):
            if nd is None:return 0
            return max(getHeight(nd.left),getHeight(nd.right)) +1
        def levelVisit(root):
            from collections import deque
            lst = deque([root])
            level = []
            h = getHeight(root)
            lv = 0
            ct = 0
            while lv<=h:
                ct+=1
                nd = lst.popleft()
                if ct >= 2**lv:
                    lv+=1
                    level.append([])
                level[-1].append(str(nd))
                if nd is not None:
                    lst.append(nd.left)
                    lst.append(nd.right)
                else:
                    lst.append(None)
                    lst.append(None)
            return level
        lines = levelVisit(self.root)
        print('-'*5+ 'level visit' + '-'*5)
        return  '\n'.join(['  '.join(line) for line in lines])
       
    def __str__(self):
        return self.display()


def genNum(n =10):
    nums =[]
    for i in range(n):
        while 1:
            d = randint(0,100)
            if d not in nums:
                nums.append(d)
                break
    #nums = [3,4,2,0,1,6]
    return nums

def buildTree(n=10,nums=None,visitor=None):
    if nums is None: nums = genNum(n)
    rbtree = redBlackTree()
    print(f'build a red-black tree using {nums}')
    for i in nums:
        if visitor:
            visitor(rbtree)
        rbtree.insert(i)
    return rbtree
def testInsert():
    def visitor(t):
        print(t)
    nums = [66, 14, 7, 2, 52, 96, 63, 51, 16, 53] 
    rbtree = buildTree(nums = nums,visitor = visitor)
    print('-'*5+ 'in-order visit' + '-'*5)
    for i,j in enumerate(rbtree.sort()):
        print(f'{i+1}: {j}')

def testSuc():
    rbtree = buildTree()
    for i in rbtree.sort():
        print(f'{i}\'s suc is {rbtree.getSuccessor(i)}')

def testDelete():
    #nums = [56, 89, 31, 29, 24, 8, 62, 96, 20, 75]  #tuple
    nums = [66, 14, 7, 2, 52, 96, 63, 51, 16, 53] 
    rbtree = buildTree(nums = nums)
    print(rbtree)
    shuffle(nums)
    for i in nums:
        print(f'deleting {i}')
        rbtree.delete(i)
        print(rbtree)

if __name__=='__main__':
    testInsert()
    #testDelete()
    #testSuc()
