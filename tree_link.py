# coding: utf-8
import os
import argparse

#命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('-p','--path',default='.')     
parser.add_argument('-f','--fileinclude',default=False)     
parser.add_argument('-d','--depth', type = int, default = 2)
#获取参数
args = parser.parse_args()
FILE = args.fileinclude
PATH = args.path
DEPTH = args.depth


def mklink(path):
    return '* [{name}]({path})'.format(name=os.path.basename(path),path=path)
def clean(paths):
    ret = []
    for path in paths:
        name = os.path.basename(path)
        if not ( name.startswith('.') or name.startswith('__')):
            ret.append(path)
    return ret

def tree(path='.',depth=2):
    li = os.listdir(path) if os.path.isdir(path) else [path]
    items = [os.path.join(path,i) for i in li if not i.startswith('.')]
    items = clean(items)
    if not FILE: items = [i for i in items if os.path.isdir(i)]
    if depth==1:
        return [mklink(path)] + [' '*4 + mklink(i) for i in items]
    else:
        uls = [tree(i,depth-1) for i in items]
        return  [mklink(path)] + [' '*4 + li for ul in uls for li in ul]


if __name__ =='__main__':
    print('\n'.join(tree(PATH,DEPTH)))
