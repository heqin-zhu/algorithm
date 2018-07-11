''' mbinary
#########################################################################
# File : manacher.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-07-06  15:56
# Description:
#########################################################################
'''

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        s2='$#'+'#'.join(s)+'#@'
        ct =[0]*(2*n+4)
        mid=1
        for cur in  range(1,2*n+2):
            if cur<mid+ct[mid]:
                ct[cur] = min(ct[2*mid-cur],mid+ct[mid]-cur)
            else:
                ct[cur]=1
            while s2[cur-ct[cur]]==s2[cur+ct[cur]]:
                ct[cur]+=1
            if cur+ct[cur] > mid+ct[mid]:mid = cur
        mx = max(ct)
        idxs = [i for i,j in enumerate(ct) if j == mx]
        p = idxs[0]
        for i in idxs:
            if s2[i]=='#':p = i
        rst =s2[p-mx+1:p+mx].replace('#','')
        return  rst
        