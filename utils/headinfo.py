''' mbinary
#########################################################################
# File : headInfo.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-07-08  14:48
# Description:
#########################################################################
'''

import os
import sys
import time
from config import HEAD
count = 0
def handleFile(path):
    global count
    head = getHead(path)
    if head =='': return
    with open(path,'r',encoding='utf8',errors='ignore') as f:
        s = f.read()
        if 'mbinary' in s:
            return
    count +=1
    name = os.path.basename(path)
    print('[{count}]: Adding head info to {name}'.format(count=count,name=name))
    with open(path,'w') as f:
        f.write(head+s)

def getHead(path):
    name = os.path.basename(path)
    # skip self or hidden file
    if name == os.path.basename(__file__) or name[0]=='.': return ''
    suf = name[name.rfind('.')+1 :]
    begin = end =''
    if suf == 'py':
        begin = end = "'''"
    elif suf in ['c','cc','cpp','java']:
        begin,end = '/*','*/'
    elif suf == 'sh':
        begin = end = '#'
    else:return ''
    timeStamp = time.localtime(os.stat(path).st_ctime)
    ctime =  time.strftime('%Y-%m-%d  %H:%M',timeStamp)
    return HEAD.format(begin=begin,end=end,ctime=ctime,name = name)

def handleDir(dirPath):
    gen = os.walk(dirPath)
    for path,dirs,files in gen:
        for f in files: handleFile(os.path.join(path,f))
if __name__ == '__main__':
    works = sys.argv[1:]
    if works==[] : works = ['.']
    for one in works:
        if not os.path.exists(one):
            print('[PathError]: {one} not exists'.format(one=one))
            continue
        if os.path.isdir(one):
            handleDir(one)
        else:
            handleFile(one)
