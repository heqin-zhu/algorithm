from functools import partial
class heap:
    def __init__(self,lst,reverse = False):
        self.data= heapify(lst,reverse)
        self.cmp = partial(lambda i,j,r:cmp(self.data[i],self.data[j],r),r=  reverse)
    def getTop(self):
        return self.data[0]
    def __getitem__(self,idx):
        return self.data[idx]
    def __bool__(self):
        return self.data != []
    def popTop(self):
        ret = self.data[0]
        n = len(self.data)
        cur = 1
        while cur * 2<=n:
            chd = cur-1
            r_idx = cur*2
            l_idx = r_idx-1
            if r_idx==n:
                self.data[chd] = self.data[l_idx]
                break
            j = l_idx if self.cmp(l_idx,r_idx)<0 else r_idx
            self.data[chd] = self.data[j]
            cur = j+1
        self.data[cur-1] = self.data[-1]
        self.data.pop()
        return ret

    def addNode(self,val):
        self.data.append(val)
        self.data = one_heapify(len(self.data)-1)


def cmp(n1,n2,reverse=False):
    fac = -1 if reverse else 1
    if n1 < n2: return -fac
    elif n1 > n2: return fac
    return 0

def heapify(lst,reverse = False):
    for i in range(len(lst)):
        lst = one_heapify(lst,i,reverse)
    return lst
def one_heapify(lst,cur,reverse = False):
    cur +=1
    while cur>1:
        chd = cur-1
        prt = cur//2-1
        if cmp(lst[prt],lst[chd],reverse)<0:
            break
        lst[prt],lst[chd] = lst[chd], lst[prt]
        cur = prt+1
    return lst
def heapSort(lst,reverse = False):
    lst = lst.copy()
    hp = heap(lst,reverse)
    ret = []
    while hp:
        ret.append(hp.popTop())
    return ret


if __name__ == '__main__':
    from random import randint
    n = randint(10,20)
    lst = [randint(0,100) for i in range(n)]
    print('random    : ', lst)
    print('small-heap: ', heapify(lst))
    print('big-heap  : ', heapify(lst,True))
    print('ascend    : ', heapSort(lst))
    print('descend   : ', heapSort(lst,True))
