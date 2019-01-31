''' mbinary
#########################################################################
# File : num_weight.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-05-19  21:36
# Description:
#########################################################################
'''

def covert(s,basefrom=10,baseto=2):
    return d2n(n2d(s,basefrom),baseto)
def n2d(s,base=16):
    ''' num of base_n(n<36) to decimal'''
    dic = {chr(i+ord('0')):i for i in range(10)}
    s=s.upper()
    if base>10:
        dic.update({chr(i+ord('A')):i+10 for i in range(26)})
    #if base in [16,8,2] :
    #    p=max(map(s.find,'OBX'))
    #   s=s[p+1:] #remove prefix of hex or bin or oct
    rst=0
    for i in s:
        rst=dic[i]+rst*base
    return rst

def d2n(n,base=16):
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



'''
>>> n2d(str(d2n(4001)))
4001
>>> d2n(n2d(str(4001)),2)
'100000000000001'
>>> covert('4001',16,2)
'100000000000001' 
'''
