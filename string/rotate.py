''' mbinary
#########################################################################
# File : rotate.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-05-19  21:54
# Description: three methods of rotating a list

1. 利用 ba=(br)^T(ar)^T=(arbr)^T，通过三次反转字符串: 即首先对序列前部分逆序，再对序列后部分逆序，再对整个序列全部逆序

2. 分组交换(尽可能使数组的前面连续几个数为所要结果):a长度大于b，将 ab 分成 a0a1b，交换 a0 和 b，得 ba1a0，只需再交换 a1和 a0。若 a 长度小于 b，将 ab 分成 ab0b1，交换 a 和 b0，得 b0ab1，只需再交换 a 和b0。通过不断将数组划分，和交换，直到不能再划分为止。分组过程与求最大公约数很相似。

3.所有序号为 (j+i*m) % n (j 表示每个循环链起始位置，i 为计数变量，m 表示左旋转位数，n 表示字符串长度)，会构成一个循环链（共有 gcd(n,m)个，gcd 为 n、m 的最大公约数），每个循环链上的元素只要移动一个位置即可，最后整个过程总共交换了 n 次（每一次循环链，是交换 n/gcd(n,m)次，总共 gcd(n,m)个循环链。所以，总共交换 n 次）。

#########################################################################
'''

def rotate(s,k,right=False):
    def reverse(a,b):
        while a<b:
            s[a],s[b]=s[b],s[a]
            a+=1
            b-=1
    n=len(s)
    k = k%n if not right else  n-k%n
    reverse(0,k-1)
    reverse(k,n-1)
    reverse(0,n-1)
    return s



def rotate2(s,k,right=False):
    def swap(a,b,c):
        for i in range(c):
            s[a+i],s[b+i] = s[b+i],s[a+i]
    def _rot(pl,pr):
        ''' swap s[pl,pr) , s[pr:]'''
        if pr==n:return
        if pr-pl<=n-pr:
            swap(pl,pr,pr-pl)
            _rot(pr,2*pr-pl)
        else:
            swap(pl,pr,n-pr)
            _rot(n-pr+pl,pr)
    n=len(s)
    k = k%n if not right else  n-k%n
    _rot(0,k)
    return s



def rotate3(s,k,right=False):
    def gcd(a,b):
        if b==0:return a
        return gcd(b,a%b)
    
    n=len(s)
    k = k%n if not right else  n-k%n
    r=gcd(n,k)
    for i in range(r):
        tmp = s[i]
        j = (i+k)%n
        while j!=i:
            s[j-k] = s[j]
            j = (j+k)%n
        s[(j-k+n)%n] = tmp
    return s


def test():
    def f(func,*args,right=False):
        print(' '.join(['testing:',func.__name__,str(args),'right=',str(right)]))
        rst = func(*args,right=right)
        print('result',rst)
        print()
    return f


if __name__=='__main__':
    s=[i for i in range(10)]
    tester= test()
    tester(rotate,s,4,right=True)
    tester(rotate,s,4)
    tester(rotate2,s,2,right=True)
    tester(rotate2,s,2)
    tester(rotate3,s,132,right=True)
    tester(rotate3,s,132)


'''
testing: rotate ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4) right= True
result [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]

testing: rotate ([6, 7, 8, 9, 0, 1, 2, 3, 4, 5], 4) right= False
result [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

testing: rotate2 ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2) right= True
result [8, 9, 0, 1, 2, 3, 4, 5, 6, 7]

testing: rotate2 ([8, 9, 0, 1, 2, 3, 4, 5, 6, 7], 2) right= False
result [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

testing: rotate3 ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 132) right= True
result [8, 9, 0, 1, 2, 3, 4, 5, 6, 7]

testing: rotate3 ([8, 9, 0, 1, 2, 3, 4, 5, 6, 7], 132) right= False
result [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
