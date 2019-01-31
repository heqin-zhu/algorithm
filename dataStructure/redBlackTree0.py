''' mbinary
#########################################################################
# File : redBlackTree.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-07-14  16:15
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
        return nd is not None and self.val == nd.val
    def setChild(self,nd,isLeft):
        if isLeft: self.left = nd
        else: self.right = nd
    def getChild(self,isLeft):
        if isLeft: return self.left
        else: return self.right
    def __bool__(self):
        return self.val is not None
    def __str__(self):
        color = 'B' if self.isBlack else 'R'
        return f'{color}-{self.val}'
    def __repr__(self):
        return f'node({self.val},isBlack={self.isBlack})'
class redBlackTree:
    def __init__(self,unique=False):
        '''if unique is True, all node'vals are unique, else there may be equal vals'''
        self.root = None
        self.unique = unique

    @staticmethod
    def checkBlack(nd):
        return nd is None or nd.isBlack
    @staticmethod
    def setBlack(nd,isBlack):
        if nd is not None:
            if isBlack is None or isBlack:
                nd.isBlack = True
            else:nd.isBlack = False
    def getParent(self,chd):
        '''note that use is to find real node when different nodes have euqiv val'''
        if self.root is chd:return None
        nd = self.root
        while nd:
            if nd>chd and  nd.left is not None:
                if nd.left is  chd: return nd
                else: nd = nd.left
            elif nd<chd and  nd.right is not None:
                if nd.right is  chd: return nd
                else: nd = nd.right
    def find(self,val):
        nd = self.root
        while nd:
            if nd.val ==val:
                return nd
            else:
                nd = nd.getChild(nd.val>val)
    def getSuccessor(self,nd):
        if nd:
            if nd.right:
                nd = nd.right
                while nd.left:
                    nd = nd.left
                return nd
            else:return self.getParent(nd)
    def setRoot(self,nd):
        if nd is not None: nd.parent=None
        self.root= nd
    def transferParent(self,origin,new):
        if origin is  self.root:
            self.root = new
        else:
            prt = self.getParent(origin)
            prt.setChild(new, prt.left is origin)
    def rotate(self,prt,chd,direction):
        '''rotate prt, and return new prt, namyly the original chd'''
        prt.setChild(chd.getChild(direction), not direction)
        chd.setChild(prt,direction)
        return chd

    def insert(self,nd):
        if nd.isBlack: nd.isBlack = False

        if self.root is None:
            self.setRoot(nd)
            self.root.isBlack = True
        else:
            parent = self.root
            while parent:
                if parent == nd : return None
                isLeft = parent > nd
                chd  = parent.getChild(isLeft)
                if chd is None:
                    parent.setChild(nd,isLeft)
                    break
                else:
                    parent = chd
            self.fixUpInsert(parent,nd)
    def fixUpInsert(self,parent,nd):
        ''' adjust color and level,  there are two red nodes: the new one and its parent'''
        while not self.checkBlack(parent):
            grand = self.getParent(parent)
            isLeftPrt = grand.left is parent 
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
                isLeftNode = parent.left is nd
                if isLeftNode ^ isLeftPrt:
                    # case 2.1 the new node is inserted in left-right or right-left form
                    #         grand               grand
                    #     parent        or            parent
                    #          nd                   nd
                    self.rotate(parent,nd,isLeftPrt)    #parent rotate
                    grand.setChild(nd,isLeftPrt)
                    nd,parent = parent,nd
                # case 2.2 the new node is inserted in left-left or right-right form
                #         grand               grand
                #      parent        or            parent
                #     nd                                nd

                # grand rotate
                
                self.rotate(grand,parent,not isLeftPrt)
                self.setBlack(grand, False)
                self.setBlack(parent, True)
                self.transferParent(grand,parent)
        self.setBlack(self.root,True)

    def copyNode(self,src,des):
        '''when deleting a node which has two kids, 
            copy its succesor's data to his position
            data exclude left, right , isBlack
        '''
        des.val = src.val
    def delete(self,val):
        '''delete node in a binary search tree'''
        if isinstance(val,node): val = val.val
        nd = self.find(val)
        if nd is None: return
        y = None
        if nd.left and nd.right:
            y= self.getSuccessor(nd)
        else:
            y = nd
        py = self.getParent(y)
        x = y.left if y.left else y.right
        if py is None:
            self.root = x
        else:
            py.setChild(x,py.left is y)
        if y != nd:
            self.copyNode(y,nd)

        if self.checkBlack(y): self.fixUpDel(py,x)

 
    def fixUpDel(self,prt,chd):
        ''' adjust colors and rotate '''
        while self.root != chd and self.checkBlack(chd):
            isLeft = prt.left is  chd 
            brother = prt.getChild(not isLeft)
            # brother is black
            lb = self.checkBlack(brother.getChild(isLeft))
            rb = self.checkBlack(brother.getChild(not isLeft))
            if  not self.checkBlack(brother):
                # case 1: brother is red.   converted to  case 2,3,4
                # prt (isLeft) rotate

                self.rotate(prt,brother,isLeft)

                self.setBlack(prt,False)
                self.setBlack(brother,True)

                self.transferParent(prt,brother)
            elif lb and rb: 
                # case 2: brother is black and two kids are black. 
                # conveted to the begin case
                self.setBlack(brother,False)
                chd = prt
                prt = self.getParent(chd)
            else:
                if  rb:
                    # case 3: brother is black and left kid is red and right child is black
                    # uncle's son is nephew, and niece for uncle's daughter
                    nephew = brother.getChild(isLeft)
                    self.setBlack(nephew,True)
                    self.setBlack(brother,False)

                    # brother (not isLeft) rotate
                    prt.setChild(nephew,not isLeft)
                    self.rotate(brother,nephew,not isLeft)
                    brother = nephew

                # case 4: brother is black and right child is red
                brother.isBlack = prt.isBlack
                self.setBlack(prt,True)
                self.setBlack(brother.getChild(not isLeft),True)

                # prt left rotate
                self.rotate(prt,brother,isLeft)

                self.transferParent(prt,brother)

                chd = self.root
        self.setBlack(chd,True)

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

    def display(self):
        def getHeight(nd):
            if nd is None:return 0
            return max(getHeight(nd.left),getHeight(nd.right)) +1
        def levelVisit(root):
            from collections import deque
            lst = deque([root])
            level = []
            h = getHeight(root)
            ct = lv = 0
            while 1:
                ct+=1
                nd = lst.popleft()
                if ct >= 2**lv:
                    lv+=1
                    if lv>h:break
                    level.append([])
                level[-1].append(str(nd))
                if nd is not None:
                    lst += [nd.left,nd.right]
                else:
                    lst +=[None,None]
            return level
        def addBlank(lines):
            width = 5
            sep = ' '*width
            n = len(lines)
            for i,oneline in enumerate(lines):
                k  = 2**(n-i) -1
                new = [sep*((k-1)//2)]
                for s in oneline:
                    new.append(s.ljust(width))
                    new.append(sep*k)
                lines[i] = new
            return lines

        lines = levelVisit(self.root)
        lines = addBlank(lines)
        li = [''.join(line) for line in lines]
        li.insert(0,'red-black-tree'.rjust(48,'-')  + '-'*33)
        li.append('end'.rjust(42,'-')+'-'*39+'\n')
        return  '\n'.join(li)
       
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
    return nums

def buildTree(n=10,nums=None,visitor=None):
    if nums is None or nums ==[]: nums = genNum(n)
    rbtree = redBlackTree()
    print(f'build a red-black tree using {nums}')
    for i in nums:
        rbtree.insert(node(i))
        if visitor:
            visitor(rbtree,i)
    return rbtree,nums
def testInsert(nums=None):
    def visitor(t,val):
        print('inserting',val)
        print(t)
    rbtree,nums = buildTree(visitor = visitor,nums=nums)
    print('-'*5+ 'in-order visit' + '-'*5)
    for i,j in enumerate(rbtree.sort()):
        print(f'{i+1}: {j}')

def testSuc(nums=None):
    rbtree,nums = buildTree(nums=nums)
    print(rbtree)
    for i in rbtree.sort():
        print(f'{i}\'s suc is {rbtree.getSuccessor(i)}')

def testDelete(nums=None):
    rbtree,nums = buildTree(nums = nums)
    print(rbtree)
    for i in nums:
        print(f'deleting {i}')
        rbtree.delete(i)
        print(rbtree)

if __name__=='__main__':
    #lst = [41,38,31,12,19,8]
    #lst.sort()
    lst = None
    lst =[45, 30, 64, 36, 95, 38, 76, 34, 50, 1] 
    testSuc()
    testInsert(lst)
    testDelete()
