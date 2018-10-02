''' mbinary
#########################################################################
# File : 8Astar.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-05-19  23:06
# Description:
#########################################################################
'''

isVisited = [0]*362880  # 0 for not visited,1 for occured,2 for visited 
fac = [1,1,2,6,24,120,720,5040,40320]
lf = len(fac)
h = [[0,1,2,1,2,3,2,3,4],
     [1,0,1,2,1,2,3,2,3],
     [2,1,0,3,2,1,4,3,2],
     [1,2,3,0,1,2,1,2,3],
     [2,1,2,1,0,1,2,1,2],
     [3,2,1,2,1,0,3,2,1],
     [2,3,4,1,2,3,0,1,2],
     [3,2,3,2,1,2,1,0,1],
     [4,3,2,3,2,1,2,1,0]]

def cantor(s):
    sum = 0
    ls = len(s)
    for i in range(ls):
        count = 0
        for j in range(i+1,ls):
            if s[i] > s[j]: count +=1
        sum += count*fac[lf-i-1]
    return sum

que = []
dir = {-3:'u',1:'r',3:'d',-1:'l'}
class state:
    flag = True
    def __init__(self,s,x,f,step=0,last=0):
        self.x = x
        self.s = list(s)
        self.step = step
        self.path = []
        self.last = last
        self.f = f
    def can(self):
        cans = [-1,1,3,-3]
        if self.last in cans :
            cans.remove(-self.last)
        if self.x<3:
            cans.remove(-3)
        if self.x>5:
            cans.remove(3)
        if self.x%3 is 0:
            cans.remove(-1)
        if self.x%3 is 2:
            cans.remove(1)
        return cans
    def move(self):
        cans = self.can()
        for i in cans:
            s = list(self.s)
            tmp = self.x + i
            s[self.x] = s[tmp]
            s[tmp] = '9'
            ct = cantor(s)
            if  isVisited[ct] != 2 :
                val = int(s[self.x])
                f = h[8][tmp] +h[val-1][self.x]-h[8][self.x]-h[val-1][tmp]+self.step+1
                new = state(s,tmp,f,self.step +1,i)
                new.path = self.path + [dir[i]]
                if isVisited[ct] == 1:
                    for i,node in enumerate(que):
                        if mew.s == node.s:
                            del que[i]
                            break
                else:isVisited[ct] = 1
                if que == []:
                    que.append(new)
                    continue
                for i,node in enumerate(que):
                    if new.f<=node.f:
                        que.insert(i,new)
def solvable(s):
    reverse = 0
    for i in range(8):
        if s[i] is '9':continue
        for j in range(i+1,9):
            if s[i]>s[j]:reverse +=1
    if reverse % 2 is 0:return True
    else:return False
def getPath(s,index):
    f = 0
    for i,j in enumerate(s):
        f+=h[int(j)-1][i]
    que.append(state(s,index,f,0,0))
    while que != []:
        cur = que.pop(0)
        ct = cantor(cur.s)
        isVisited[ct] = 2
        if ct is 0:
            return cur.path
        cur.move()
def info():
    print('input a 3x3 matrix in one line')
    print('from left to right,from up to down') 
    print('such as 56831247x  represent matrix as follow')
    print('5  6  8\n3  1  2\n4  7  x')
    print('then, if it has, I will print the path of moving x to reach state as follows')
    print('1  2  3\n4  5  6\n7  8  x')
    print('print q to quit')

from random import shuffle
case = list('12345678x')
def genCase():
    tmp = case.copy()
    shuffle(tmp)
    print(f'Using random data: {tmp}')
    index = -1
    for i,j in enumerate(tmp):
        if j=='x':
            index = i
            break
    tmp[index] = '9'
    return tmp,index
def isValid(li):
    for i in '123456789':
        if not i in li:
            print('Invalid Input')
            return False
    return True

def run():
    while 1:
        print('\n\n'+'-'*10+'Game Begins'+ '-'*10)
        info()
        s=input('input: ') 
        if s=='q' or s=='Q' or s=='quit':
            break
        index = s.find('x')
        li = list(s)
        if index != -1:
            li[index] = '9'
        if not isValid(li):
            li, index = genCase()
        if solvable(li):
            print(''.join(getPath(li,index)))
        else:print('unsolvable')


if __name__ == '__main__':
    run()
