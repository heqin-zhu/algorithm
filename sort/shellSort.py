''' mbinary
#########################################################################
# File : shellSort.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-07-06  16:30
# Description:
#########################################################################
'''

def shellSort(s,gaps=None):
    if gaps is None:
        gaps = [127,63,31,15,7,3,1]
    n = len(s)
    for gap in gaps:
        for j in range(gap,n):
            cur = j
            num = s[j]
            while cur>=gap and num < s[cur-gap]:
                s[cur] = s[cur-gap]
                cur-=gap
            s[cur] = num
    return s

if __name__=='__main__':
    from random import randint
    import sys
    n = 20
    if len(sys.argv)>1:
        n = int(sys.argv[1])
    nums = [randint(1,100) for i in range(n)]
    print(nums)
    print(shellSort(nums))
