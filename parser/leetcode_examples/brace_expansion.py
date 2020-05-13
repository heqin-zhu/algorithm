import re
from collections import namedtuple

token = namedtuple('token', ['type', 'value'])


left = r'(?P<LEFT>\{)'
right = r'(?P<RIGHT>\})'
word = r'(?P<WORD>[a-z]+)'
comma = r'(?P<COMMA>\,)'
blank = r'(?P<BLANK>\s)'
pt = re.compile('|'.join([left, right, word, comma, blank]))


def genToken(s):
    scanner = pt.scanner(s)
    for i in iter(scanner.match, None):
        if i.lastgroup != 'BLANK':
            yield token(i.lastgroup, i.group(0))


class parser:
    '''gramar
        expr -> item | item ',' expr
        item -> factor | factor item
        factor -> WORD | '{' expr '}'
    '''

    def match(self, tp):
        # print(self.p.value)
        if tp == self.p.type:
            val = self.p.value
            try:
                self.p = next(self.gen)
            except StopIteration:
                self.p = None
            except Exception as e:
                print(e)
            return val
        else:
            raise Exception(f"[Error]: {tp} expected, got {self.p.type}")

    def parse(self, s):
        self.gen = genToken(s)
        self.p = next(self.gen)
        st = self.expr()
        return sorted(list(st))

    def expr(self):
        ret = self.item()
        while self.p and self.p.type == 'COMMA':
            self.match('COMMA')
            ret = ret.union(self.item())
        return ret

    def item(self):
        ret = self.factor()
        while self.p and self.p.type in ['WORD', 'LEFT']:
            sufs = self.factor()
            new = set()
            for pre in ret:
                for suf in sufs:
                    new.add(pre+suf)
            ret = new
        return ret

    def factor(self):
        if self.p.type == 'LEFT':
            self.match('LEFT')
            ret = self.expr()
            self.match('RIGHT')
            return ret
        return {self.match('WORD')}


class Solution:
    def braceExpansionII(self, expression):
        return parser().parse(expression)


if __name__ == '__main__':
    sol = Solution()
    li = ["{a,b}{c{d,e}}", "{{a,z}, a{b,c}, {ab,z}}", "{a,b}c{d,e}f"]
    for i in li:
        print('>>>', i)
        print(sol.braceExpansionII(i))
