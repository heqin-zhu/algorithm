import unittest
from token_scanner import gen_token

class TestTokenScanner(unittest.TestCase):
    def Test_gen_token(self):
        li = [i for i in gen_token('int a;')]
        ans = [Token('NAME','int',1),Token('NAME','a',1),Token('SEMICOLON',';',1)]
        self.assertEqual(li,ans)

if __name__=='__main__':
    unittest.main()
