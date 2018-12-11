''' mbinary
#########################################################################
# File : permute_divide_and_conquer.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-11-25  12:23
# Description:
#########################################################################
'''
def permute(lst,n):
    ''' O(n!), optimal'''
    if n==1:print(lst)
    else:
        for i in range(n):
            lst[i],lst[n-1] = lst[n-1],lst[i]
            permute(lst,n-1)
            lst[i],lst[n-1] = lst[n-1],lst[i]

if __name__=='__main__':
    n = 3
    permute([i for i in range(n)],n)
