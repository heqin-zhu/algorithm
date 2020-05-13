import re
from collections import namedtuple
left = r'(?P<LEFT>\()'
right = r'(?P<RIGHT>\))'
word = r'(?P<WORD>[a-z][a-z0-9]*)'
num = r'(?P<NUM>(\-)?\d+)'
blank = r'(?P<BLANK>\s+)'
pt = re.compile('|'.join([left, right, word, num, blank]))

token = namedtuple('token', ['type', 'value'])


def genToken(s):
    scanner = pt.scanner(s)
    for i in iter(scanner.match, None):
        if i.lastgroup != 'BLANK':
            yield token(i.lastgroup, i.group(0))


class parser(object):
    '''grammar:
        S-> '(' expr ')'
        expr -> [mult|add] item item | let {word item } item 
        item -> num | word| S 
    '''

    def config(self,s):
        if s:
            self.token = [i for i in genToken(s)]
            self.lookahead = 0
            self.vars = []

    def parse(self, s):
        self.config(s)
        try:
            return self.S()
        except Exception as e:
            return e

    def match(self, curType):
        sym = self.token[self.lookahead]
        if sym.type == curType:
            self.lookahead += 1
            return sym.value
        self.errorinfo(f'Expected {curType}, got {sym.value}')

    def errorinfo(self, s, k=None):
        if k is None:
            k = self.lookahead
        pre = ' '.join([t.value for t in self.token[:k]])
        suf = ' '.join([t.value for t in self.token[k:]])
        print(pre+' '+suf)
        print(' '*(len(pre)+1)+'^'*len(self.token[k].value))
        raise Exception(s)

    def readVar(self, var):
        for dic in self.vars[::-1]:
            if var in dic:
                return dic[var]
        self.errorinfo(f"Undefined varible '{var}'", self.lookahead-1)

    def S(self):
        self.vars.append({})
        self.match('LEFT')
        ret = self.expr()
        self.match('RIGHT')
        self.vars.pop()
        return ret

    def expr(self):
        op = self.match('WORD')
        if op == 'let':
            while self.token[self.lookahead].type != 'RIGHT':
                if self.token[self.lookahead].type == 'WORD':
                    var = self.match('WORD')
                    if self.token[self.lookahead].type == 'RIGHT':
                        return self.readVar(var)
                    else:
                        self.vars[-1][var] = self.item()
                else:
                    return self.item()
        elif op in {'mult', 'add'}:
            a = self.item()
            b = self.item()
            if op == 'mult':
                return a*b
            elif op == 'add':
                return a+b
        else:
            self.errorinfo('Unknown keyword', self.lookahead-1)

    def item(self):
        if self.token[self.lookahead].type == 'WORD':
            return self.readVar(self.match('WORD'))
        elif self.token[self.lookahead].type == 'NUM':
            return int(self.match('NUM'))
        else:
            return self.S()


class Solution(object):
    def evaluate(self, expression: str) -> int:
        return parser().parse(expression)


if __name__ == "__main__":
    sol = Solution()

    exprs = ['(add -1 2)',
             '(let x -2 y x y)',
             '(mult 3 (add 2 3))',
             '(let x 2 (mult x 5))',
             '(let x 2 (mult x (let x 3 y 4 (add x y))))',
             '(let x 2 x 3 x)',
             '(let x 2 (add (let x 3 (let x 4 x)) x))',
             '(let a1 3 b2 (add a1 1) b2)',
             'add 1 2)',  # wrongs
             '(asd 1 2)',
             '(let a 1 b)',
             '(let a 1 b 2)'
             ]
    for e in exprs:
        print('>>>', e)
        print(sol.evaluate(e))
