#coding: utf-8
''' mbinary
#######################################################################
# File : subarraySum.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2020-04-20  16:49
# Description: 子数组累加和
#######################################################################
'''
from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    dic = {0: 1}
    sm = 0
    count = 0
    for i in range(len(nums)):
        sm += nums[i]
        if((sm-k) in dic):
            count += dic[sm-k]
        if(sm in dic):
            dic[sm] += 1
        else:
            dic[sm] = 1
    return count
