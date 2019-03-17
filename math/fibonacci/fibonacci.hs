{-''' mbinary
#######################################################################
# File : fibonacci.hs
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.github.io
# Github: https://github.com/mbinary
# Created Time: 2019-02-03  19:42
# Description: matrix pow and fast pow:
    calculate big number fibonacci item. for negative item, use f(n) = f(n+2)-f(n+1)
#######################################################################
-}
module Fibonacci where

fib :: Integer -> Integer
fib  n = let p =  if n>0 then n-2 else 2-n
             mat = if n>0 then [1,1,1,0] else [0,1,1,-1]
             m = matrix_pow mat p
          in m!!0+m!!1
          
          
matrix_pow mat n = if n<=0 then [1,0,0,1]
                   else let v = if (mod n 2==0) then [1,0,0,1] else mat
                            m2 = matrix_mul mat mat
                            remain = matrix_pow m2  (div n 2)
                         in matrix_mul v remain          
                   
matrix_mul a b = [ a!!0 * b!!0 +a!!1 * b!!2,a!!0 * b!!1 +a!!1 * b!!3,a!!2 * b!!0 +a!!3 * b!!2, a!!2 * b!!1+a!!3 * b!!3]                   
