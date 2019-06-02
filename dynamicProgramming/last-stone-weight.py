#coding: utf-8
''' mbinary
#######################################################################
# File : last-stone-weight.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2019-05-28  23:30
# Description:
leetcode 1049: https://leetcode-cn.com/problems/last-stone-weight-ii/

有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。

#######################################################################
'''

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sm = sum(stones)
        ans = sm//2
        dp = [0]*(ans+1)
        for x in stones:
            for j in range(ans,x-1,-1):
                dp[j] = max(dp[j],dp[j-x]+x)
    return sm-2*dp[ans]
