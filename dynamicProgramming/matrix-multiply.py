''' mbinary
#########################################################################
# File : matrix-multiply.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-08-24  21:24
# Description:
#########################################################################
'''

def adjustOrd(sizes):
    ''' adjust the chain-multiply of matrix, sizes=[row1,row2,..,rown,coln]'''
    n = len(sizes)
    if n<3: return 
