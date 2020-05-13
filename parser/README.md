# parser
先进行词法分析，然后进行语法分析，然后编写递归下降程序。可以将代码形成框架，词法分析每次只需要改变正则表达式部分即可，语法分析代码只需要实现语法对应的函数.
我这里列举了4个题目，都可以这样解答。


* [Lisp 语法解析](#lisp-语法解析)
    * [题目](#题目)
    * [语法](#语法)
    * [代码](#代码)
* [原子的数量](#原子的数量)
    * [题目](#题目-1)
    * [语法](#语法-1)
    * [代码](#代码-1)
* [花括号展开2](#花括号展开2)
    * [题目](#题目-2)
    * [语法](#语法-2)
    * [代码](#代码-2)
* [基本计算器4](#基本计算器4)
    * [题目](#题目-3)
    * [语法](#语法-3)
    * [代码](#代码-3)
* [更多](#更多)

## [Lisp 语法解析](https://leetcode-cn.com/problems/parse-lisp-expression/)
### 题目

给定一个类似 Lisp 语句的表达式 expression，求出其计算结果。

表达式语法如下所示:

- 表达式可以为整数，let 语法，add 语法，mult 语法，或赋值的变量。表达式的结果总是一个整数。
- (整数可以是正整数、负整数、0)
- let 语法表示为 (let v1 e1 v2 e2 ... vn en expr), 其中 let 语法总是以字符串 "let" 来表示，接下来会跟随一个或多个交替变量或表达式，也就是说，第一个变量 v1 被分配为表达式 e1 的值，第二个变量 v2 被分配为表达式 e2 的值，以此类推；最终 let 语法的值为 expr 表达式的值。
- add 语法表示为 (add e1 e2)，其中 add 语法总是以字符串 "add" 来表示，该语法总是有两个表达式 e1、e2, 该语法的最终结果是 e1 表达式的值与 e2 表达式的值之和。
- mult 语法表示为 (mult e1 e2) ，其中 mult 语法总是以字符串 "mult" 表示， 该语法总是有两个表达式 e1、e2，该语法的最终结果是 e1 表达式的值与 e2 表达式的值之积。
- 在该题目中，变量的命名以小写字符开始，之后跟随 0 个或多个小写字符或数字。为了方便，"add"，"let"，"mult" 会被定义为 "关键字"，不会在表达式的变量命名中出现。
- 最后，要说一下作用域的概念。计算变量名所对应的表达式时，在计算上下文中，首先检查最内层作用域（按括号计），然后按顺序依次检查外部作用域。我们将保证每一个测试的表达式都是合法的。有关作用域的更多详细信息，请参阅示例。

```
>>> (let x -2 y x y)
-2
>>> (mult 3 (add 2 3))
15
>>> (let x 2 (mult x 5))
10
>>> (let x 2 (mult x (let x 3 y 4 (add x y))))
14
>>> (let x 2 x 3 x)
3
>>> (let x 2 (add (let x 3 (let x 4 x)) x))
6
>>> (let a1 3 b2 (add a1 1) b2)
4
```
### 语法
```
S-> '(' expr ')'
expr -> [mult|add] item item | let {word item } item 
item -> num | word| S 
```

### 代码
```python [lisp-收起]
```
```python [lisp-展开]
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
```


## [原子的数量](https://leetcode-cn.com/problems/number-of-atoms)
### 题目

给定一个化学式 formula（作为字符串），返回每种原子的数量。

原子总是以一个大写字母开始，接着跟随 0 个或任意个小写字母，表示原子的名字。

如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。

两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。

一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2) 3 是化学式。

给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。
```
>>> K4(ON(SO3)2)2
K4N2O14S4
>>> Mg(OH)2
H2MgO2
```

### 语法
```
S-> item | S item
item -> word | word num | '(' S ')' num 
```

### 代码
```python [atom-收起]
```
```python3 [atom-展开]
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
```

## [花括号展开2](https://leetcode-cn.com/problems/brace-expansion-ii/)
### 题目
如果你熟悉 Shell 编程，那么一定了解过花括号展开，它可以用来生成任意字符串。

花括号展开的表达式可以看作一个由 花括号、逗号 和 小写英文字母 组成的字符串，定义下面几条语法规则：

如果只给出单一的元素 x，那么表达式表示的字符串就只有 "x"。 
例如，表达式 {a} 表示字符串 "a"。
而表达式 {ab} 就表示字符串 "ab"。
当两个或多个表达式并列，以逗号分隔时，我们取这些表达式中元素的并集。
例如，表达式 {a,b,c} 表示字符串 "a","b","c"。
而表达式 {a,b},{b,c} 也可以表示字符串 "a","b","c"。
要是两个或多个表达式相接，中间没有隔开时，我们从这些表达式中各取一个元素依次连接形成字符串。
例如，表达式 {a,b}{c,d} 表示字符串 "ac","ad","bc","bd"。
表达式之间允许嵌套，单一元素与表达式的连接也是允许的。
```
>>> {a,b}{c{d,e}}
['acd', 'ace', 'bcd', 'bce']
>>> {{a,z}, a{b,c}, {ab,z}}
['a', 'ab', 'ac', 'z']
>>> {a,b}c{d,e}f
['acdf', 'acef', 'bcdf', 'bcef']
```
### 语法
```
expr -> item | item ',' expr
item -> factor | factor item
factor -> WORD | '{' expr '}'
```

### 代码
```python [brace-收起]
```
```python3 [brace-展开]
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
```
## [基本计算器4](https://leetcode-cn.com/problems/basic-calculator-iv/)
### 题目
给定一个表达式 expression 如 expression = "e + 8 - a + 5" 和一个求值映射，如 {"e": 1}（给定的形式为 evalvars = ["e"] 和 evalints = [1]），返回表示简化表达式的标记列表，例如 ["-1*a","14"]

表达式交替使用块和符号，每个块和符号之间有一个空格。
块要么是括号中的表达式，要么是变量，要么是非负整数。
块是括号中的表达式，变量或非负整数。
变量是一个由小写字母组成的字符串（不包括数字）。请注意，变量可以是多个字母，并注意变量从不具有像 "2x" 或 "-x" 这样的前导系数或一元运算符 。
表达式按通常顺序进行求值：先是括号，然后求乘法，再计算加法和减法。例如，expression = "1 + 2 * 3" 的答案是 ["7"]。

输出格式如下：

对于系数非零的每个自变量项，我们按字典排序的顺序将自变量写在一个项中。例如，我们永远不会写像 “b*a*c” 这样的项，只写 “a*b*c”。
项的次数等于被乘的自变量的数目，并计算重复项。(例如，"a*a*b*c" 的次数为 4。)。我们先写出答案的最大次数项，用字典顺序打破关系，此时忽略词的前导系数。
项的前导系数直接放在左边，用星号将它与变量分隔开 (如果存在的话)。前导系数 1 仍然要打印出来。
格式良好的一个示例答案是 ["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"] 。
系数为 0 的项（包括常数项）不包括在内。例如，“0” 的表达式输出为 []。
```
>>> ((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a)) [] []
['-1*a*a*b*b', '2*a*a*b*c', '-1*a*a*c*c', '1*a*b*b*b', '-1*a*b*b*c', '-1*a*b*c*c', '1*a*c*c*c', '-1*b*b*b*c', '2*b*b*c*c', '-1*b*c*c*c', '2*a*a*b', '-2*a*a*c', '-2*a*b*b', '2*a*c*c', '1*b*b*b', '-1*b*b*c', '1*b*c*c', '-1*c*c*c', '-1*a*a', '1*a*b', '1*a*c', '-1*b*c']
>>> e + 8 - a + 5 ['e'] [1]
['-1*a', '14']
```

### 语法
```
expr -> expr {'+'|'-'} term | term
term -> term '*' item | item
item -> num | var | '(' expr ')'
```

### 代码

```python [cal-收起]
```
```python3 [cal-展开]
import re
from collections import namedtuple
left = r'(?P<LEFT>\()'
right = r'(?P<RIGHT>\))'
var = r'(?P<VAR>[a-z]+)'
num = r'(?P<NUM>\d+)'
add = r'(?P<ADD>\+)'
sub = r'(?P<SUB>\-)'
mul = r'(?P<MUL>\*)'
ws = r'(?P<WS> +)'
pt = re.compile('|'.join([left, right, var, ws, num, add, sub, mul]))

token = namedtuple('token', ['type', 'value'])


def genToken(s):
    scanner = pt.scanner(s)
    for i in iter(scanner.match, None):
        if i.lastgroup != 'WS':
            yield token(i.lastgroup, i.group(0))


class parser(object):
    '''grammar
        expr -> expr {'+'|'-'} term | term
        term -> term '*' item | item
        item -> num | var | '(' expr ')'
    '''

    def __init__(self, s, vars):
        self.token = [i for i in genToken(s)]
        self.lookahead = 0
        self.var = vars

    def parse(self):
        dic = self.term()
        # terminate symbol
        while self.lookahead < len(self.token) and not self.isType('RIGHT'):
            assert self.isType('SUB', 'ADD')
            sign = 1 if self.match() == '+' else -1
            var = self.term()
            for i in var:
                if i in dic:
                    dic[i] += var[i]*sign
                else:
                    dic[i] = var[i]*sign
        return dic

    def match(self, curType=None):
        sym = self.token[self.lookahead]
        # print(sym,curType)
        if curType is None or sym.type == curType:
            self.lookahead += 1
            return sym.value
        raise Exception('Invalid input string')

    def isType(self, *s):
        sym = self.token[self.lookahead]
        return any(sym.type == i for i in s)

    def term(self):
        li = []
        dic = self.item()
        while self.lookahead < len(self.token) and self.isType('MUL'):
            self.match()
            li.append(self.item())
        for d2 in li:
            newDic = {}
            for v1 in dic:
                for v2 in d2:
                    s = ''
                    if v1 == '':
                        s = v2
                    elif v2 == '':
                        s = v1
                    else:
                        s = '*'.join(sorted(v1.split('*')+v2.split('*')))
                    if s in newDic:
                        newDic[s] += dic[v1]*d2[v2]
                    else:
                        newDic[s] = dic[v1]*d2[v2]
            dic = newDic
        return dic

    def item(self):
        if self.isType('NUM'):
            return {'': int(self.match())}
        elif self.isType('VAR'):
            name = self.match()
            if name in self.var:
                return {'': self.var[name]}
            else:
                return {name: 1}
        elif self.isType('LEFT'):
            self.match()
            dic = self.parse()
            self.match('RIGHT')
            return dic
        else:
            print(self.token[self.lookahead])
            raise Exception('invalid string')


class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        self.var = dict(zip(evalvars, evalints))
        dic = parser(expression, self.var).parse()
        n = dic.pop('') if '' in dic else 0
        ret = []
        li = sorted(dic, key=lambda s: (-s.count('*'), s))
        for i in li:
            if dic[i] != 0:
                s = str(dic[i])
                ret.append(s + ('*'+i) if i else s)
        if n != 0:
            ret.append(str(n))
        return ret


if __name__ == '__main__':
    sol = Solution()
    exprs = [
        "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))", "e + 8 - a + 5"]
    names = [[], ["e"]]
    vars = [[], [1]]
    for i, j, k in zip(exprs, names, vars):
        print('>>>', i, j, k)
        print(sol.basicCalculatorIV(i, j, k))
```

## 更多
- [迷你语法分析器](https://leetcode-cn.com/problems/mini-parser/)
- [字符串解码](https://leetcode-cn.com/problems/decode-string/)

