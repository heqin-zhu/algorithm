''' mbinary
#########################################################################
# File : sunday.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-07-11  15:26
# Description: 字符串模式匹配, sunday 算法, kmp 的改进
#               pattern matching for strings using sunday algorithm
#########################################################################
'''


def getPos(pattern):
    dic = {}
    for i, j in enumerate(pattern[::-1]):
        if j not in dic:
            dic[j] = i
    return dic


def find(s, p):
    dic = getPos(p)
    ps = pp = 0
    ns = len(s)
    np = len(p)
    while ps < ns and pp < np:
        if s[ps] == p[pp]:
            ps, pp = ps+1, pp+1
        else:
            idx = ps + np-pp
            if idx >= ns:
                return -1
            ch = s[idx]
            if ch in dic:
                ps += dic[ch]+1-pp
            else:
                ps = idx+1
            pp = 0
    if pp == np:
        return ps-np
    else:
        return -1


def findAll(s, p):
    ns = len(s)
    np = len(p)
    i = 0
    ret = []
    while s:
        print(s, p)
        tmp = find(s, p)
        if tmp == -1:
            break
        ret.append(i+tmp)
        end = tmp+np
        i += end
        s = s[end:]
    return ret


def randStr(n=3):
    return [randint(ord('a'), ord('z')) for i in range(n)]


def test(n):
    s = randStr(n)
    p = randStr(3)
    str_s = ''.join((chr(i) for i in s))
    str_p = ''.join((chr(i) for i in p))
    n1 = find(s, p)
    n2 = str_s.find(str_p)  # 利用已有的 str find 算法检验
    if n1 != n2:
        print(n1, n2, str_p, str_s)
        return False
    return True


if __name__ == '__main__':
    from random import randint
    n = 1000
    suc = sum(test(n) for i in range(n))
    print('test {n} times, success {suc} times'.format(n=n, suc=suc))
