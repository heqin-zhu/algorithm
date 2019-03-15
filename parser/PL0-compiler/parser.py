'''
#########################################################################
# File : parser.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-11-04  19:50
# Description:
#########################################################################
'''
import sys
import argparse
from math import e,pi,log
from random import randint
from functools import reduce
from token_scanner import gen_token,Token
from operator import eq,ge,gt,ne,le,lt, not_,and_,or_,lshift,rshift, add,sub,mod,mul,pow,abs,neg


parser = argparse.ArgumentParser()


parser.add_argument('-i','--instruction',help="output instructions",action='store_true')
parser.add_argument('-s','--stack',help="output data stack when executing each instruction",action='store_true')
parser.add_argument('-t','--token',help="output tokens when parsing",action='store_true')
parser.add_argument('-v','--varible',help="output varibles for every static environment",action='store_true')
parser.add_argument('-f','--file',help="compile and run codes. \n Without this arg, enter interactive REPL",type=str)

args = parser.parse_args()

FILE = args.file
SHOWINS = args.instruction
SHOWSTACK = args.stack
SHOWVAR = args.varible
SHOWTOKEN = args.token


WHILE = Token('NAME','while')
THEN = Token('NAME','then')
ELSE = Token('NAME','else')
DO = Token('NAME','do')
END = Token('NAME','end')
ASSIGN = Token('ASSIGN',':=')
EQ = Token('EQ','=')
LEFT = Token('LEFT','(')
RIGHT = Token('RIGHT',')')
COMMA=Token('COMMA',',')
SEMICOLON = Token('SEMICOLON',';')
PERIOD = Token('PERIOD','.')
COLON = Token('COLON',':')

class symbol:
    '''symbols for const, varible, function name'''
    def __init__(self,name,varType,value=None,level=None,addr = None):
        self.name = name
        self.type = varType
        self.value = value
        self.level = level
        self.addr=addr
    def __str__(self):
        if self.type=='FUNC':
            return "({}, {}, {})".format(self.type,self.name,self.addr)
        elif self.type=='VAR':
            return "({}, {}={}, {})".format(self.type,self.name,self.value,self.addr)
        else:
            return "({}, {}={})".format(self.type,self.name,self.value)
    def __repr__(self):
        return "symbol('{}','{}',{},{},{})".format(self.name,self.type,self.value,self.level,self.addr)
class stack:
    '''emulate a stack that with pre-allocated space'''
    def __init__(self,lst,size=1000):
        self.lst = lst.copy()
        self.top=0
        self.lst+=[0]*(size-len(lst))

    def push(self,val):
        self.top+=1
        if self.top>=len(self.lst):
            raise Exception('[Error]: data stack overflow')
        self.lst[self.top]=val
    def pop(self):
        self.top -=1
        return self.lst[self.top+1]
    def __setitem__(self,k,val):
        self.lst[k]=val
    def __getitem__(self,k):
        return self.lst[k]
    def __str__(self):
        return str(self.lst)
    def __repr__(self):
        return 'stack({})'.format(self.lst)
class instruction:
    def __init__(self,name,levelDiff,addr):
        self.name=name
        self.levelDiff=levelDiff
        self.addr=addr
    def __str__(self):
        s = self.addr
        if type(self.addr)==str:
            s =repr(self.addr)
        return '{}   {}   {}'.format(self.name.ljust(4),self.levelDiff,s)
class closure:
    '''environment for every function, including a dict of symbols and pointing to outer environment'''
    def __init__(self,items=None,outer=None):
        self.outer =outer
        if items is None:self.items=dict()
        else: self.items  = items
        self.varNum=0
    def __getitem__(self,key):
        cur = self
        while cur is not None:
            if key in cur.items:
                return cur.items[key]
            cur = cur.outer
    def __setitem__(self,key,val):
        if key in self.items:raise Exception('[Error]: {} has been defined'.format(key))
        if val.type=='VAR':
            self.varNum+=1
        self.items[key] = val
    def __contains__(self,key):
        return key in self.items
    def __iter__(self):
        return iter(self.items.values())
    def __repr__(self):
        li = [str(i) for i in self.items.values()]
        return '\n'.join(li)

class parser(object):
    def __init__(self,tokens=None,syms=None,codes=None):
        self.tokens = [] if tokens is None else tokens
        self.codes = [] if codes is None else codes
        self.pointer = 0
        self.level = 0
        self.ip=0
        self.codes=[]
        self.initSymbol(syms)
    def initSymbol(self,syms=None):
        if syms is None: syms=[symbol('E','CONST',e,0),symbol('PI','CONST',pi,0)]
        self.closure=closure()
        self.curClosure = self.closure
        for i in syms:
            self.addSymbol(i.name,i.type,i.value)
    def addSymbol(self,var,varType,value=None):
        sym = symbol(var,varType,value,self.level,self.curClosure.varNum+3)
        self.curClosure[var]=sym
        return sym
    def getSymbol(self,var):
        sym = self.curClosure[var]
        if sym is None:
            self.errorDefine(var)
        return sym
    def genIns(self,f,l,a):
        self.codes.append(instruction(f,l,a))
        self.ip+=1
        return self.ip-1
    def errorInfo(self):
        '''when parsing codes and encountering error, 
            print whole line in which this error is
            and print error information
        '''
        def tkstr(tk):
            if tk.type=='STR':return repr(tk.value)
            return str(tk.value)
        tk = self.tokens[self.pointer]
        a=b = self.pointer
        lineno = tk.lineNum
        n = len(self.tokens)
        while a>=0 and self.tokens[a].lineNum == lineno:
            a -=1
        while b<n and self.tokens[b].lineNum == lineno:
            b +=1
        s1 = ' '.join([tkstr(t) for t in self.tokens[a+1:self.pointer]])
        s2 = ' '.join([tkstr(t) for t in self.tokens[self.pointer:b]])
        print('line {}: {} {}'.format(lineno,s1,s2))
        print(' '*(len(s1)+8+len(str(lineno)))+'^'*len(tk.value))
        return tk
    def errorIns(self,ins,pc):
        print('[Error]: Unknown instruction {}: {}  '.format(pc,ins))
    def errorDefine(self,var):
        raise Exception('[Error]: "{}" is not defined'.format(var))
    def errorArg(self,n1,n2):
        raise Exception('[Error]: Expected {} args, but {} given'.format(n1,n2))
    def errorExpect(self,s):
        raise Exception('[Error]: Expected {}, got "{}"'.format(s,self.tokens[self.pointer].value))
    def errorLoop(self,s):
        raise Exception('[Error]: "{}" outside loop'.format(s))
    def match(self,sym=None):
        if SHOWTOKEN:
            print(self.tokens[self.pointer])
        if sym is None \
           or (sym.type=='NUM' and self.isType('NUM')) \
           or sym==self.tokens[self.pointer]:
            self.pointer+=1
            return self.tokens[self.pointer-1]
        self.errorExpect('"'+sym.value+'"')
    def parse(self,tokens=None):
        '''parse codes from tokens, then generate instructions and execute them'''
        self.ip=0
        self.codes=[]
        self.pointer=0
        if tokens is not None: self.tokens = tokens
        if self.tokens is None:return
        try:
            self.program()
            if SHOWINS:
                print('     ins   i   a')
                for i,ins in enumerate(self.codes):print(str(i).ljust(4),ins)
            if self.pointer != len(self.tokens):
                raise Exception ('[Error]: invalid syntax')
        #try:pass
        except Exception as e:
            self.errorInfo()
            print(e)
            return
        result =self.interpret()
        for sym in self.closure:
            if sym.type=='VAR':
                sym.value = result[sym.addr-3]
        res = result[self.closure.varNum:]
        if res!=[]: print('result: ',end='')
        for i in res:
            print(i,end='; ')
        if res!=[]: print()

    def isType(self,s):
        '''judge the lookahead symbol'''
        if self.pointer == len(self.tokens):sym = Token('EOF','$')
        else:    sym = self.tokens[self.pointer]
        if s in self.reserved: return sym.value==s.lower()
        if s =='NAME' and sym.value.upper() in self.reserved: return False
        return sym.type ==s
    def isAnyType(self,lst):
        return any([self.isType(i) for i in lst])
    def wantType(self,s):
        if not self.isType(s): self.errorExpect(s)
    def backpatching(self,ip,addr,levelDiff=None):
        self.codes[ip].addr= addr
        if levelDiff is not None:self.codes[ip].levelDiff=levelDiff
    def program(self):
        '''the begining of a grammar, to implement'''
        pass
    def interpret(self):
        '''the code executing emulator'''
        pass

class PL0(parser):
    def __init__(self,tokens=None,syms=None,codes=None,level=0):
        '''init pc, closure, reserved keywords, operators'''
        super().__init__()
        self.reserved={'FUNC','PRINT','RETURN','BEGIN','END','IF','THEN','FOR','ELIF','ELSE','WHILE','DO','BREAK','CONTINUE','VAR','CONST','ODD','RANDOM','SWITCH','CASE','DEFAULT'}
        self.bodyFirst= self.reserved.copy()
        self.bodyFirst.remove('ODD')
        self.relationOPR= {'EQ':eq,'NEQ':ne,'GT':gt,'LT':lt,'GE':ge,'LE':le} # odd
        self.conditionOPR = {'AND':and_,'OR':or_, 'NOT':not_}
        self.conditionOPR.update(self.relationOPR)
        self.arithmeticOPR = {'ADD':add,'SUB':sub,'MOD':mod,'MUL':mul,'POW':pow,'DIV':lambda x,y:x/y,'INTDIV':lambda x,y:round(x)//round(y) }
        self.bitOPR = {'LSHIFT':lambda x,y:round(x)<<round(y),'RSHIFT':lambda x,y:round(x)>>round(y),'BITAND':lambda x,y:round(x)&round(y), 'BITOR':lambda x,y:round(x)|round(y),'BITNOT':lambda x:~round(x)}
        self.binaryOPR = dict()
        self.binaryOPR.update(self.conditionOPR)
        del self.binaryOPR['NOT']
        self.binaryOPR.update(self.arithmeticOPR)
        self.binaryOPR.update(self.bitOPR)
        del self.binaryOPR['BITNOT']
        self.unaryOPR = {'NEG':neg,'NOT':not_,'BITNOT':lambda x:~round(x),'FAC':lambda x:reduce(mul,range(1,round(x)+1),1),'ODD':lambda x:round(x)%2==1, 'RND':lambda x:randint(0,x),'INT':round}#abs

    def program(self):
        self.enableJit = False
        self.genIns('INT',0,None)
        self.genIns('JMP',0,None)
        ip= self.body()
        self.backpatching(0,self.curClosure.varNum+3)
        self.backpatching(1,ip)
        self.match(PERIOD)
        self.genIns('RET',0,0)
    def body(self):
        while 1:
            if self.isType('CONST') or self.isType('VAR'):
                tp = self.match().value.upper()
                while 1:
                    self.wantType('NAME')
                    name = self.match().value
                    val = None
                    if self.isType('EQ'):
                        self.match(EQ)
                        minus = False
                        if self.isType('SUB'):
                            self.match()
                            minus=True
                        self.wantType('NUM')
                        val = float(self.match().value)
                        if minus: val = -val
                    self.addSymbol(name,tp,val)
                    if self.isType('SEMICOLON'):
                        self.match()
                        break
                    self.match(COMMA)
            elif self.isType('FUNC'):
                self.match()
                self.wantType('NAME')
                name = self.match().value
                args = self.arg_list()
                sym = self.addSymbol(name,'FUNC',self.ip)
                self.level +=1
                sym.closure=closure(outer=self.curClosure)
                self.curClosure = sym.closure
                beginIp = self.genIns( 'INT',0,None)
                narg = len(args)
                sym.argNum = narg
                ips=[]
                for arg in args:
                    self.addSymbol(arg,'VAR')
                    ips.append(self.genIns('MOV',None,None))
                self.body()
                nvar = self.curClosure.varNum
                self.curClosure = self.curClosure.outer
                span1 = nvar -narg
                span2 = 3+nvar
                for i ,ip in enumerate(ips):
                    self.backpatching(ip,span1+i,span2+i)
                self.match(SEMICOLON)
                self.backpatching(beginIp,nvar+3)
                self.level -=1
                self.genIns('RET',0,0)
            else:break
        ret = self.ip
        if SHOWVAR:
            print('level: {}'.format(self.level))
            print(self.curClosure)
            print()
        for sym in self.curClosure:
            if sym.type=='VAR' and sym.value is not None:
                self.genIns('LIT',0,sym.value)
                self.genIns('STO',0,sym.addr)
        if not  self.isType('PERIOD'):
            for ip in self.sentence()['RETURN']:
                self.backpatching(ip,self.ip)
        return ret
    def arg_list(self):
        self.match(LEFT)
        li = []
        if not self.isType('RIGHT'):
            self.wantType('NAME')
            li=[self.match().value]
        while self.isType('COMMA'):
            self.match()
            self.wantType('NAME')
            li.append(self.match().value)
        self.match(RIGHT)
        return li
    def real_arg_list(self):
        self.match(LEFT)
        ct=0
        if not  self.isType('RIGHT'):
            self.sentenceValue()
            ct+=1
        while self.isType('COMMA'):
            self.match()
            self.sentenceValue()
            ct+=1
        self.match(RIGHT)
        return ct
    def sentence_list(self,outerLoop=None):
        ret = self.sentence(outerLoop)
        while self.isType('SEMICOLON'):
            self.match()
            dic=self.sentence(outerLoop)
            for i in ['BREAK','CONTINUE','RETURN']:
                ret[i] = ret[i].union(dic[i])
        return ret
    def formatStr(self,s):
        n = len(s)
        i = 0
        segs = []
        last = 0
        while i<n:
            if s[i]=='%' and i+1<n:
                if i>0 and s[i-1]=='\\':
                    segs.append(s[last:i-1])
                    last=i
                elif s[i+1] in 'df':
                    segs.append(s[last:i])
                    segs.append('%{}'.format(s[i+1]))
                    last = i+2
                    i +=1
            i+=1
        if last<n:
            segs.append(s[last:])
        return segs

    def sentence(self,outerLoop=None):
        ret ={'BREAK':set(),'CONTINUE':set(),'RETURN':set()}
        if self.isType('BEGIN'):
            self.match()
            ret = self.sentence_list(outerLoop)
            self.match(END)
        elif self.isType('PRINT'):
            self.match()
            self.match(LEFT)
            if not self.isType('RIGHT'):
                self.wantType('STR')
                s  = self.match().value
            else:s=''
            segs= self.formatStr(s)
            n = 0
            for seg in segs:
                if seg in ['%d','%f']:
                    self.match(COMMA)
                    self.sentenceValue()
                    if seg=='%d': self.genIns('OPR',1,'INT')#type convert
                    n +=1
                else:
                    for i in seg: self.genIns('LIT',0,i)
            self.genIns('LIT',0,'\n')
            unitNum = sum(len(i) for i in segs) -n +1
            self.genIns('INT',2,unitNum)
            self.match(RIGHT)
        elif self.isType('BREAK'):
            if outerLoop is None: self.errorLoop('break')
            self.match()
            ret['BREAK'].add(self.genIns('JMP',0,None))
        elif self.isType('CONTINUE'):
            self.match()
            if outerLoop is None: self.errorLoop('continue')
            ret['CONTINUE'].add(self.genIns('JMP',0,None))
        elif self.isType('IF'):
            self.match()
            self.sentenceValue()
            self.match(THEN)
            jpcIp = self.genIns('JPC',0,None)
            ret = self.sentence(outerLoop)
            jmpIps = []
            while self.isType('ELIF'):
                self.match()
                ip = self.genIns('JMP',0,None)
                jmpIps.append(ip)
                self.backpatching(jpcIp,self.ip)
                self.sentenceValue()
                jpcIp = self.genIns('JPC',0,None)
                self.match(THEN)
                dic=self.sentence(outerLoop)
                for i in ['BREAK','CONTINUE','RETURN']:
                    ret[i] = ret[i].union(dic[i])

            if self.isType('ELSE'):
                self.match()
                ip = self.genIns('JMP',0,None)
                jmpIps.append(ip)
                self.backpatching(jpcIp,self.ip)
                dic=self.sentence(outerLoop)
                for i in ['BREAK','CONTINUE','RETURN']:
                    ret[i] = ret[i].union(dic[i])
            else:
                self.backpatching(jpcIp,self.ip)
            for ip in jmpIps:
                self.backpatching(ip,self.ip)
        elif self.isType('SWITCH'):
            self.match()
            self.sentenceValue()
            self.genIns('POP',0,1)
            while self.isType('CASE'):
                self.match()
                self.genIns('PUSH',0,1)
                self.sentenceValue()
                self.genIns('OPR',2,'EQ')
                if self.isType('COMMA'):
                    self.match()
                    self.sentenceValue()
                    self.genIns('PUSH',0,1)
                    self.genIns('OPR',2,'EQ')
                    self.genIns('OPR',2,'OR')
                jpcIp = self.genIns('JPC',0,None)
                self.match(COLON)
                if not self.isType('CASE'):
                    dic = self.sentence()
                self.backpatching(jpcIp,self.ip)
            #if self.isType('DEFAULT'):
            #    self.match()
            #    self.match(COLON)
            #    self.sentence()
        elif self.isType('DO'):
            self.match()
            jpcIp =None
            beginIp = self.ip
            ret  = self.sentence(1)
            self.match(WHILE)
            self.sentenceValue()
            jpcIp = self.genIns('JPC',0,None)
            self.genIns('JMP',0,beginIp)
            self.backpatching(jpcIp,self.ip)
            for jmpip in ret['BREAK']:
                self.backpatching(jmpip,self.ip)
            for jmpip in ret['CONTINUE']:
                self.backpatching(jmpip,beginIp)
        elif self.isType('WHILE') or self.isType('FOR'):
            tp = self.match()
            beginIp = jpcIp =None
            if tp.value=='while':
                beginIp = self.ip
                self.sentenceValue()
                jpcIp = self.genIns('JPC',0,None)
                self.match(DO)
            else:
                self.match(LEFT)
                if not self.isType('SEMICOLON'):
                    self.assignment()
                self.match(SEMICOLON)
                beginIp = self.ip
                if not self.isType('SEMICOLON'):
                    self.sentenceValue()
                    jpcIp = self.genIns('JPC',0,None)
                self.match(SEMICOLON)
                if not self.isType('RIGHT'):
                    self.assignment()
                self.match(RIGHT)
            ret  = self.sentence(1)
            self.genIns('JMP',0,beginIp)
            self.backpatching(jpcIp,self.ip)
            for jmpip in ret['BREAK']:
                self.backpatching(jmpip,self.ip)
            for jmpip in ret['CONTINUE']:
                self.backpatching(jmpip,beginIp)
        elif self.isType('RETURN'): # retrun sentence
            self.match()
            self.sentenceValue()
            self.genIns('POP',0,0)
            ret['RETURN'].add(self.genIns('JMP',0,None))
        elif self.isAnyType(['SEMICOLON','END','ELSE']):pass # allow blank sentence: namely   ; ;; 
        elif self.isAssignment() : # this must be the last to be checked in sentences
            self.assignment()
        else:
            self.sentenceValue()
        return ret
    def funcall(self):
        name = self.match().value
        sym = self.getSymbol(name)
        saved = self.curClosure
        self.curClosure = sym.closure
        n2= self.real_arg_list()
        self.curClosure = saved
        if sym.argNum!=n2:
            self.errorArg(sym.argNum,n2)
        self.genIns('CAL',abs(self.level-sym.level),sym.value)
        self.genIns('INT',1,n2)
        self.genIns('PUSH',0,0)
    def sentenceValue(self):
        self.condition()
    def isAssignment(self):
        return self.isType('NAME') \
           and self.pointer+1<len(self.tokens)\
           and self.tokens[self.pointer+1]==ASSIGN

    def assignment(self):
        varLst = []
        while self.isAssignment():
            varLst .append(self.match().value)
            self.match(ASSIGN)
        self.sentenceValue()
        sym0 = self.getSymbol(varLst[0])
        lastLevel=abs(self.level-sym0.level)
        lastAddr = sym0.addr
        self.genIns('STO',lastLevel,sym0.addr)
        for var in varLst[1:]:
            sym = self.getSymbol(var)
            if sym.type=='CONST':
                raise Exception('[Error]: Const "{}" can\'t be reassigned'.format(sym.name))
            self.genIns('LOD',lastLevel,lastAddr)
            lastLevel = abs(self.level-sym.level)
            lastAddr = sym.addr
            self.genIns('STO',lastLevel,sym.addr)
    def condition(self):
        self.condition_and()
        while self.isType('OR'):
            self.match()
            self.condition_and()
            self.genIns('OPR',2,'OR')
        if self.isType('QUESTION'): # 即条件表达式  condition ? expr1 : expr2
            self.match()
            ip = self.genIns('JPC',0,None)
            self.sentenceValue()
            ip2 = self.genIns('JMP',0,None)
            self.match(COLON)
            self.backpatching(ip,self.ip)
            self.sentenceValue()
            self.backpatching(ip2,self.ip)
    def condition_and(self):
        self.condition_not()
        while self.isType('AND'):
            self.match()
            self.condition_not()
            self.genIns('OPR',2,'AND')
    def condition_not(self):
        ct = 0
        while self.isType('NOT'):
            self.match()
            ct+=1
        self.condition_unit()
        if ct%2==1:
            self.genIns('OPR',1,'NOT')
    def condition_unit(self):
        if self.isType('ODD'):
            self.match()
            self.expression()
            self.genIns('OPR',1,'ODD')
            return
        self.expression()  # 允许 表达式作为逻辑值, 即 非0 为真, 0 为假
        if self.isAnyType(self.relationOPR):
            op = self.match().type
            self.expression()
            self.genIns('OPR',2,op)
    def expression(self):
        self.level1()
        while 1:   # interval production,  optimized tail recursion and merged it
            if self.isType('RSHIFT'):
                self.match()
                self.level1()
                self.genIns('OPR',2,'RSHIFT')
            elif self.isType('LSHIFT'):
                self.match()
                self.level1()
                self.genIns('OPR',2,'LSHIFT')
            elif self.isType('BITAND'):
                self.match()
                self.level1()
                self.genIns('OPR',2,'BITAND')
            elif self.isType('BITOR'):
                self.match()
                self.level1()
                self.genIns('OPR',2,'BITOR')
            else:
                return
    def item(self):
        if self.isType('NUM'):
            val = float(self.match().value)
            self.genIns('LIT',0,val)
        #elif self.isType('STR'):
        #    val = self.match().value
        #    self.genIns('LIT',0.,val)
        elif self.isType('LEFT'):
            self.match()
            self.sentenceValue()
            self.match(RIGHT)
        elif self.isType('SUB'):
            self.match()
            self.item()
            self.genIns('OPR',1,'NEG')
        elif self.isType('ADD'):
            self.match()
            self.item()
        elif self.isType('BITNOT'):
            self.match()
            self.item()
            self.genIns('OPR',1,'BITNOT')
        elif self.isType('RANDOM'):
            self.match()
            self.match(LEFT)
            if self.isType('RIGHT'):
                self.genIns('LIT',0,1<<16)
            else:
                self.expression()
            self.match(RIGHT)
            self.genIns('OPR',1,'RND')
        elif self.isType('NAME'):
            if self.tokens[self.pointer+1] == LEFT:
                self.funcall()
            else:
                name = self.match().value
                if name=='true':
                    self.genIns('LIT',0,True)
                elif name=='false':
                    self.genIns('LIT',0,False)
                else:
                    sym = self.getSymbol(name)
                    if sym.type=='CONST':
                        self.genIns('LIT',0,sym.value)
                    else:
                        self.genIns('LOD',abs(self.level-sym.level),sym.addr)
        else:
            self.errorExpect('a value')
    def level1(self):
        self.level2()
        while 1:
            if self.isType('ADD'):
                self.match()
                self.level2()
                self.genIns('OPR',2,'ADD')
            elif self.isType('SUB'):
                self.match()
                self.level2()
                self.genIns('OPR',2,'SUB')
            else: return
    def level2(self):
        self.level3()
        while 1:
            if self.isType('MUL'):
                self.match()
                self.level3()
                self.genIns('OPR',2,'MUL')
            elif self.isType('DIV'):
                self.match()
                self.level3()
                self.genIns('OPR',2,'DIV')
            elif self.isType('INTDIV'):
                self.match()
                self.level3()
                self.genIns('OPR',2,'INTDIV')
            elif self.isType('MOD'):
                self.match()
                self.level3()
                self.genIns('OPR',2,'MOD')
            else:return
    def level3(self):
        self.level4()
        if self.isType('POW'):
            self.match()
            self.level3()
            self.genIns('OPR',2,'POW')
        return
    def level4(self):
        self.item()
        while self.isType('FAC'):#factorial
            self.match()
            self.genIns('OPR',1,'FAC')
    def interpret(self):
        def base(stk,curLevel,levelDiff):
            for i in range(levelDiff):
                curLevel = stk[curLevel]
            return curLevel

        stk = stack([0,0,0])
        stk.top=2
        b = pc=0
        regs=[None,None]
        while 1:
            ins = self.codes[pc]
            pc+=1
            if ins.name=='INT':
                if ins.levelDiff==0: stk.top+=ins.addr-3 # allocate space
                elif ins.levelDiff==1: stk.top-=ins.addr # rewind stack top bakc n spaces
                elif ins.levelDiff==2: #print 
                    stk.top = stk.top-ins.addr+1
                    for i in range(ins.addr):
                        print(stk[stk.top+i],end='')
                    stk.top-=1
                else:self.errorIns(ins,pc-1)
            elif ins.name=='LIT':
                stk.push(ins.addr)
            elif ins.name=='STO':
                pos = base(stk,b,ins.levelDiff)+ins.addr
                stk[pos]= stk.pop()
            elif ins.name=='LOD':
                val = stk[base(stk,b,ins.levelDiff)+ins.addr]
                stk.push(val)
            elif ins.name=='MOV':
                stk[stk.top-ins.addr] = stk[stk.top-ins.levelDiff]
            elif ins.name=='JMP':
                pc = ins.addr
            elif ins.name=='JPC':
                if not stk.pop():
                    pc = ins.addr
            elif ins.name=='CAL':
                stk.push(base(stk,b,ins.addr))  # static link  
                stk.push(b)       # dynamic link
                b = stk.top-1
                stk.push(pc)      # return addr
                pc = ins.addr
            elif ins.name=='OPR':
                if ins.levelDiff==1:
                    stk[stk.top] = self.unaryOPR[ins.addr](stk[stk.top])
                elif ins.levelDiff==2:
                    arg2 = stk.pop()
                    arg1 = stk[stk.top]
                    stk[stk.top] = self.binaryOPR[ins.addr](arg1,arg2)
                else:self.errorIns(ins,pc-1)
            elif ins.name=='RET':
                pc = stk[b+2]
                if pc!=0: stk.top=b-1
                b = stk[b+1]
            elif ins.name=='POP':
                regs[ins.addr] = stk.pop()
            elif ins.name=='PUSH':
                stk.push(regs[ins.addr])
            else:
                self.errorIns(ins,pc-1)
            if SHOWSTACK: print(str(pc).ljust(5),ins,stk[:stk.top+1])
            if pc==0:break
        return stk[3:stk.top+1]

def getCode(inStream):
    lines = []
    eof = False
    while 1:
        line = inStream.readline()
        if line=='':
            eof = True
            break
        if line.rstrip(' \n\r\t')=='': continue
        lines.append(line)
        p = line.find('//')
        if p==-1 and line.rstrip('\n\r \t').endswith('.'):break
    if eof and len(lines)==0: raise EOFError
    return lines,inStream

def testFromStdIO():
    cal = PL0()
    while 1:
        sys.stdout.write('>> ')
        sys.stdout.flush()
        lines,sys.stdin = getCode(sys.stdin)
        s = ''.join(lines)
        tk =[i for i in  gen_token(s)]
        if tk==[]:continue
        res = cal.parse(tk)
        if res is not None: print(res)
def testFromFile(f):
    cal = PL0()
    with open(f,'r') as fp:
        try:
            while 1:
                lines,fp = getCode(fp)
                if len(lines)==1: print('>>',lines[0].strip('\n\r'))
                else:
                    print('>> codes: ')
                    for i,l in enumerate(lines):
                        print(str(i+1).ljust(5),l,end='')
                    print()
                tk =[i for i in  gen_token(''.join(lines))]
                if tk ==[]:continue
                res = cal.parse(tk)
                if res is not None: print(res)
        except EOFError:
            pass
if __name__=='__main__':
    if FILE: testFromFile(FILE)
    else:  testFromStdIO()
