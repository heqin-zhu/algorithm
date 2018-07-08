def quickSort(lst):
    '''A optimized version of Hoare partition'''
    def partition(a,b):
        pivot = lst[a]
        while a!=b:
            while a<b and lst[b]>pivot: b-=1
            if a<b:
                lst[a] = lst[b]
                a+=1
            while a<b and lst[a]<pivot: a+=1
            if a<b:
                lst[b] = lst[a]
                b-=1
        lst[a] = pivot
        return a
    def  _sort(a,b):
        if a>=b:return 
        mid = (a+b)//2
        # 三数取中值置于第一个作为 pivot
        if (lst[a]<lst[mid]) ^ (lst[b]<lst[mid]): lst[a],lst[mid] = lst[mid],lst[a]  # lst[mid] 为中值
        if (lst[a]<lst[b]) ^ (lst[b]>lst[mid]): lst[a],lst[b] = lst[b],lst[a] # lst[b] 为中值
        i = partition(a,b)
        _sort(a,i-1)
        _sort(i+1,b)
    _sort(0,len(lst)-1)
    return lst
def quickSort2(lst):
    '''A version of partition from <Introduction of Algorithm>,  a little bit slow'''
    def partition(a,b):
        pivot = lst[b]
        j = a-1
        for i in range(a,b):
            if lst[i]<=pivot:
                j+=1
                if i!=j: lst[i], lst[j] = lst[j], lst[i]
        lst[j+1],lst[b] = lst[b],lst[j+1]
        return j+1
    def  _sort(a,b):
        if a>=b:return 
        mid = (a+b)//2
        # 三数取中值置于第一个作为 pivot
        if (lst[a]<lst[mid]) ^ (lst[b]<lst[mid]): lst[b],lst[mid] = lst[mid],lst[b]  # lst[mid] 为中值
        if (lst[a]>lst[b]) ^ (lst[a]>lst[mid]): lst[a],lst[b] = lst[b],lst[a] # lst[b] 为中值
        i = partition(a,b)
        _sort(a,i-1)
        _sort(i+1,b)

    _sort(0,len(lst)-1)
    return lst
def quickSort3(lst):
    '''A  rear recursive optimization version'''
    def partition(a,b):
        pivot = lst[b]
        j = a-1
        for i in range(a,b):
            if lst[i]<=pivot:
                j+=1
                if i!=j: lst[i], lst[j] = lst[j], lst[i]
        lst[j+1],lst[b] = lst[b],lst[j+1]
        return j+1
    def  _sort(a,b):
        while a<b:
            mid = (a+b)//2
            # 三数取中值置于第一个作为 pivot
            if (lst[a]<lst[mid]) ^ (lst[b]<lst[mid]): lst[b],lst[mid] = lst[mid],lst[b]  # lst[mid] 为中值
            if (lst[a]>lst[b]) ^ (lst[a]>lst[mid]): lst[a],lst[b] = lst[b],lst[a] # lst[b] 为中值
            i = partition(a,b)
            _sort(a,i-1)
            a = i+1
    _sort(0,len(lst)-1)
    return lst

from time import time
def timer(func,lst,n=100):
    t = time()
    for i in range(n):func(lst)
    t = time()-t
    print('{}: {}s'.format(func.__name__,t))
    return t

if __name__ == '__main__':
    from random import randint
    print('5000 items, repeat 100 times for each')
    lst = [randint(0,100) for i in range(5000)]
    timer(quickSort,lst.copy())
    timer(quickSort2,lst.copy())
    timer(quickSort3,lst.copy())

    lst = [randint(0,100) for i in range(15)]
    print(lst)
    print(quickSort(lst.copy()))
    print(quickSort2(lst.copy()))
    print(quickSort3(lst.copy()))


