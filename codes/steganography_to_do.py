''' mbinary
#########################################################################
# File : steganography_to_do.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-07-06  15:57
# Description:
#########################################################################
'''

from PIL import Image
from skimage import color
import numpy as np
import matplotlib.pyplot as plt
import math
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('picture')
parser.add_argument('-f','file')
parser.add_argument('-s','string')

args = parser.parse_args()

PIC = args.picture
FILE = args.file
STR = args.string


class steganography:
    def __init__(self,picture):
        self.pic = poicture

    def handlePixel(self,target,attach):
        '''对一个像素进行隐写 ,attach是要处理的数值，允许在0~9'''
        a,b,c =  target
        pa,pb,pc = attach
        return a%10+pa,b%10+pb,c%10+pc
    def d2n(self,n,base=16):
        ''' num of base_n(n<36) to decimal'''
        dic = {i:chr(i+ord('0')) for i in range(10)}
        if base>10:
            dic.update({i+10:chr(i+ord('A')) for i in range(26)})
        rst=[]
        while n!=0:
            i=int(n/base)
            rst.append(dic[n-i*base])
            n=i
        return ''.join(rst[::-1])
    def changeBody(self,path):
        self.pic = path
    def encryptPic(self,content,base =8):
        '''将bytes内容content隐写到self.picture中  base can be different value, default 8'''
        body = np .array (Image.open(self.pic))
        attach = np.array(content)
        r,c, _ = body.shape
        ar,ac,_ = attach.shape
        
        raise Exception('信息量太大，不能隐写在此图片中，换张更大的图片')
    def encryptStr(self,content):
        body = np.array (Image.open(self.pic))
        r,c,d = body.shape
        btay = bytearray(content)
        length = len(btay)
        if length*8 > (r-1)*c:raise Exception('信息量太大，不能隐写在此图片中，换张更大的图片')
    def getContent(self,file=None,s=None):
        '''get the bytes ,  file is prior to str'''
        byte = b''
        if not file:
            if not s:
                s = input('输入要隐写的信息')
            byte = encode(STR,'utf-8')
        else:byte = open(FILE,'wb').read()
        return byte

if __name__ =='__main__':
    
    PIC
