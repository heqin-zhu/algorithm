import re
from collections import namedtuple
left = r'(?P<LEFT>\()'
right = r'(?P<RIGHT>\))'
word = r'(?P<WORD>[A-Z][a-z]*)'
num = r'(?P<NUM>\d+)'
pt = re.compile('|'.join([left, right, word, num]))

token = namedtuple('token', ['type', 'value'])


def genToken(s):
    scanner = pt.scanner(s)
    for i in iter(scanner.match, None):
        yield token(i.lastgroup, i.group(0))


class parser:
    '''grammar:
        S-> item | S item
        item -> word | word num | '(' S ')' num 
    '''

    def match(self, curType):
        sym = self.token[self.lookahead]
        if sym.type == curType:
            self.lookahead += 1
            return sym.value
        raise Exception('Invalid input string')

    def parse(self, s):
        self.token = [i for i in genToken(s)]
        self.lookahead = 0
        return self.S()
    def S(self):
        dic = {}
        while self.lookahead < len(self.token) and self.token[self.lookahead].type != 'RIGHT':
            cur = self.item()
            for i in cur:
                if i in dic:
                    dic[i] += cur[i]
                else:
                    dic[i] = cur[i]
        return dic

    def item(self):
        if self.token[self.lookahead].type == 'WORD':
            ele = self.match('WORD')
            n = 1
            if self.lookahead < len(self.token) and self.token[self.lookahead].type == 'NUM':
                n = int(self.match('NUM'))
            return {ele: n}
        elif self.token[self.lookahead].type == 'LEFT':
            self.match('LEFT')
            dic = self.S()
            self.match('RIGHT')
            n = int(self.match("NUM"))
            for i in dic:
                dic[i] *= n
            return dic
        else:
            print(self.token[self.lookahead])
            raise Exception('invalid string')


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        dic = parser().parse(formula)
        return ''.join(c+str(dic[c]) if dic[c] != 1 else c for c in sorted(dic.keys()))


if __name__ == "__main__":
    li = ["K4(ON(SO3)2)2","Mg(OH)2"]
    sol = Solution()
    for s in li:
        print('>>>',s)
        print(sol.countOfAtoms(s))
