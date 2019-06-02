#coding: utf-8
''' mbinary
#######################################################################
# File : addNegaBin.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2019-06-02  22:32
# Description:

给出基数为 -2 的两个数 arr1 和 arr2，返回两数相加的结果。

数字以 数组形式 给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如，arr = [1,1,0,1] 表示数字 (-2)^3 + (-2)^2 + (-2)^0 = -3。数组形式 的数字也同样不含前导零：以 arr 为例，这意味着要么 arr == [0]，要么 arr[0] == 1。

返回相同表示形式的 arr1 和 arr2 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。

eg
输入：arr1 = [1,1,1,1,1], arr2 = [1,0,1]
输出：[1,0,0,0,0]
解释：arr1 表示 11，arr2 表示 5，输出表示 16
#######################################################################
'''
from nega import nega

def addNegaBin(arr1: list, arr2: list) -> list:
    if len(arr1) < len(arr2):
        arr1, arr2 = arr2, arr1
    for i in range(-1, -len(arr2) - 1, -1):
        if arr1[i] == 1 and arr2[i] == 1:
            arr1[i] = 0
            mux = 0
            for j in range(i - 1, -len(arr1) - 1, -1):
                if arr1[j] == mux:
                    mux = 1 - mux
                    arr1[j] = mux
                else:
                    arr1[j] = mux
                    break
            else:
                arr1 = [1, 1] + arr1

        elif arr1[i] == 0 and arr2[i] == 1:
            arr1[i] = arr2[i]
        #print(arr1,arr2,i)
    while len(arr1) > 1 and arr1[0] == 0:
        arr1.pop(0)
    return arr1

if __name__=='__main__':
    while 1:
        print("input q to quit or input x1 x2: ")
        s = input()
        if s=='q':
            break
        n1,n2 =[int(i) for i in  s.split()]
        l1,l2 = nega(n1),nega(n2)
        print(n1,l1)
        print(n2,l2)
        print(f'{n1}+{n2}={n1+n2}: {addNegaBin(l1,l2)}')
