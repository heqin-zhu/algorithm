'''
#########################################################################
# File : token_scanner.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-09-17  22:20
# Description: 
#########################################################################
'''

import re
STR = r'[\'\"](?P<STR>.*?)[\'\"]' # not completely correct yet
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d*\.\d+|\d+)' # note that don't use \d+|\d*\.\d+

ASSIGN = r'(?P<ASSIGN>\:\=)'

# ODD = r'(?P<ODD>odd )'
EQ = r'(?P<EQ>=)'
NEQ = r'(?P<NEQ>!=)'
GT = r'(?P<GT>\>)'
LT = r'(?P<LT>\<)'
GE = r'(?P<GE>\>\=)'
LE = r'(?P<LE>\<\=)'

BITNOT = r'(?P<BITNOT>\~)'
BITOR = r'(?P<BITOR>\|)'
BITAND = r'(?P<BITAND>\&)'
RSHIFT = r'(?P<RSHIFT>\>\>)'
LSHIFT = r'(?P<LSHIFT>\<\<)'

AND = r'(?P<AND>\&\&)'
NOT = r'(?P<NOT>\!)'
OR = r'(?P<OR>\|\|)'

ADD = r'(?P<ADD>\+)'
SUB=r'(?P<SUB>\-)'

MUL = r'(?P<MUL>\*)'
INTDIV = r'(?P<INTDIV>\/\%)'
MOD = r'(?P<MOD>\%)'
DIV = r'(?P<DIV>\/)'

POW = r'(?P<POW>\^)'
FAC=r'(?P<FAC>\!)'  #factorial

COLON = r'(?P<COLON>\:)'
COMMA = r'(?P<COMMA>\,)'
SEMICOLON = r'(?P<SEMICOLON>\;)'
PERIOD = r'(?P<PERIOD>\.)'
QUESTION = r'(?P<QUESTION>\?)'
LEFT=r'(?P<LEFT>\()'
RIGHT=r'(?P<RIGHT>\))'
WS = r'(?P<WS>\s+)'


COMMENT = r'(?P<COMMENT>//[^\r\n]*|/\*.*?\*/)'
  # note that lt,gt should be after le,ge and rshift, lshift
li = [STR,NUM, AND,OR,BITAND,BITOR,BITNOT,RSHIFT,LSHIFT,
      EQ,NEQ,GE,LE,LT,GT,\
      SUB,MOD, ADD, MUL,INTDIV,DIV, POW,FAC,NOT,\
      COMMA,SEMICOLON,PERIOD, QUESTION,WS,LEFT,RIGHT,\
      ASSIGN,COLON,NAME] # COLON behind ASSIGN
master_pat = re.compile('|'.join(li),re.DOTALL)

class Token:
    def __init__(self,tp,value,lineNum=None):
        self.type = tp
        self.value= value
        self.lineNum = lineNum
    def __eq__(self,tk):
        return self.type==tk.type and self.value==tk.value
    def __repr__(self):
        s = self.value if self.type!='STR' else '"{}"'.format(repr(self.value))
        return '({},{},{})'.format(self.type,s,self.lineNum)

def gen_token(text):
    li = text .split('\n')
    beginComment=False
    for i,line in enumerate(li):
        s = line.lstrip()
        if beginComment:
            p = s.find('*/')
            if p!=-1: beginComment=False
            if p!=-1 and p+2<len(s):
                s = s[p+2:]
            else:
                continue
        p = s.find('//')
        if p!=-1:s =  s[:p]
        if s=='' : continue
        p = s.find('/*')
        if p!=-1:
            beginComment=True
            s =s[:p]
        scanner = master_pat.scanner(s)
        for m in iter(scanner.match,None):
            tok = Token(m.lastgroup,m.groupdict()[m.lastgroup],i+1)
            if tok.value=='exit':exit()
            if tok.type!='WS' and tok.type!='COMMENT':
                yield tok
if __name__ =='__main__':
    while 1:
        expr = input('>> ')
        for i in gen_token(expr):
            print(i)
