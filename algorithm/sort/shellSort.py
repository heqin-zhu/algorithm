''' mbinary
#########################################################################
# File : shellSort.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-07-06  16:30
# Description:
#########################################################################
'''

def shellSort(s,inc=None):
    if inc is None:inc = [1,3,5,7,11,13,17,19]
    num = len(s)
    inc.sort(reverse=True)
    for i in inc:
        for j in range(i,num):
            cur = j
            while cur>=i and s[j] > s[cur-i]:
                s[cur] = s[cur-i]
                cur-=i
            s[cur] = s[j]
    return s
