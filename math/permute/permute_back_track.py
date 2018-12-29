''' mbinary
#########################################################################
# File : permute_back_track.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-11-25  12:32
# Description:
#########################################################################
'''
def permute(n):
    def _util(lst,i):
        if i==n:print(lst)
        else:
            for j in range(i,n):
                lst[i],lst[j]=lst[j],lst[i]
                _util(lst,i+1)
                lst[i],lst[j]=lst[j],lst[i]
    _util([i for i in range(n)],0)

if __name__=='__main__':
    permute(5)
