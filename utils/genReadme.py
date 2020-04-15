''' mbinary
#########################################################################
# File : genReadme.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-12-11  15:53
# Description:
#########################################################################
'''
# coding: utf-8
from tree import tree
from argparse import ArgumentParser
from config import README

parser = ArgumentParser()

parser.add_argument('-p', '--path', default='.', help='path to walk')
parser.add_argument('-f', '--fileinclude', action='store_true',
                    default=True, help='if has, list files and dirs, else only dirs')
parser.add_argument('-d', '--depth', type=int, default=2)
# 获取参数
args = parser.parse_args()
FILE = args.fileinclude
PATH = args.path
DEPTH = args.depth


idxs = tree(PATH, DEPTH, FILE)
s = README.format(index='\n'.join(idxs))
with open('README.md', 'w') as f:
    f.write(s)
