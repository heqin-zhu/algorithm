from pickle import load,dump
from random import randint

def next(dic,s,li):
    if s[-1] not in dic: 
        if len(li)>10:print(li)
        return
    for i in dic[s[-1]]:
        if i in li: continue
        next(dic,i,li+[i])
def gen(dic):
    for i in dic:
        for j in dic[i]:
            next(dic,j,[j])

class node:
    def __init__(self,val):
        self.val = val
        self.chd={}
        self.prt={}
    def to(self,nd):
        if nd.val not in self.chd:
            self.chd[nd.val] = nd
            nd.prt[self.val] = self
    def __getitem__(self,i):
        return self.val[i]
    def __str__(self):
        return '{}->{}'.format(self.val,list(self.chd.keys()))
    def __repr__(self):
        return 'node({})'.format(self.val)
    def __len__(self):
        return len(self.chd)
class graph:
    def __init__(self):
        self.data = {}
    def addNode(self,s):
        if s not in self.data:
            nd = node(s)
            for i,j in self.data.items():
                if i[-1]==nd[0]: j.to(nd)
                if i[0]== nd[-1]: nd.to(j)
            self.data[s] = nd

    def __str__(self):
        print()
    def __getitem(self,i):
        return self.data[i]
def clean(dic):
    g = graph()
    for i in dic:
        for j in dic[i]:
            g.addNode(j)

    dic = {}
    for i,j in g.data.items():
        if j.chd=={} and j.prt=={}: continue
        if i[0] in dic: dic[i[0]].append(i)
        else:dic[i[0]] = [i]

    with open('four.pk','wb') as f:
        dump(dic,f)
def play():
    def once(last):
        word = last[-1]
        if word[-1] not in dic:
            if len(last)>1: 
                print('{}-> '.format(last))
                print('-'*5+'end'+'-'*5)
            return  
        else:
            print('{}-> '.format(last))
        lst = dic[word[-1]]
        for i,j in enumerate(lst):
            print('{}. {}'.format(i,j))
        print('q. quit')
        choose = input('>>> ')
        if choose == 'q':return
        once(last+[lst[int(choose)%len(lst)]])

    lst = dic[li[randint(0,n-1)]]
    word = lst[randint(0,len(lst)-1)]
    once([word])
if __name__ =='__main__':
    dic=None
    with open('four.pk','rb') as f:
        dic = load(f)
    li = list(dic.keys())
    n = len(li)
    while 1:play()
