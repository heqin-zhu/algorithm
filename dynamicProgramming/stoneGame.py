#coding: utf-8
''' mbinary
#######################################################################
# File : stoneGame.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-12-14  14:32
# Description:
    亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。
    亚历克斯和李轮流进行. 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
    那么先手一定会赢吗? 是的, 求出先手比后手多的石子数.
    leetcode-cn 877: https://leetcode-cn.com/problems/stone-game/
#######################################################################
'''
def stoneGame(li):
    '''li: list, len(li)%2==0, sum(li)%2==1'''
   def f(p,q):
       ret = dp[p][q]
       if ret is None:
           if p+1==q:
               ret =  abs(li[p]-li[q])
           else:
               # max min     
               # take the first one
               n1 = li[p] + min(-li[p+1]+f(p+2,q),-li[q]+f(p+1,q-1))
               # take the last one
               n2 = li[q] + min(-li[p]+f(p+1,q-1),-li[q-1]+f(p,q-2))
               ret =  max(n1,n2)
           dp[p][q] = ret
       #print(li[p:q+1],ret)
       return ret
   n = len(li)
   dp = [[None for i in range(n)] for i in range(n)]
   return f(0,n-1)
