''' mbinary
#########################################################################
# File : test_token_scanner.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2019-04-16  09:41
# Description:
#########################################################################
'''
import unittest
from token_scanner import gen_token

class TestTokenScanner(unittest.TestCase):
    def Test_gen_token(self):
        li = [i for i in gen_token('int a;')]
        ans = [Token('NAME','int',1),Token('NAME','a',1),Token('SEMICOLON',';',1)]
        self.assertEqual(li,ans)

if __name__=='__main__':
    unittest.main()
