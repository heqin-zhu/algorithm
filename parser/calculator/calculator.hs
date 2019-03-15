module Calculator where

-- calculator, integers, operators: +-*/
-- "2 / 2 + 3 * 4 - 13" ==  0
-- "4 + 3 * 4 / 3 - 6 / 3 * 3 + 8"  == 10
-- <grammar>
-- expr   -> factor | expr {+|-} factor
-- factor -> num    | factor  {*|/} num

evaluate :: String -> Double
evaluate  s = expr.factor.getNum.filter (\x->x/=' ') $s


getNum "" = (0,"")
getNum s = let n = length.takeWhile (\x->'0' <=x && x<='9') $s
               (num,res) = splitAt n s
               x = read num::Double
           in (x,res)
                     
factor (x,s) = if s=="" || s!!0 =='+' || s!!0 =='-' then (x,s)
               else let op = head s
                        (y,s2) = getNum $tail s
                        z = if op=='*' then x*y else x/y
                    in   factor (z,s2)

expr (x,s) =   if s=="" then x
               else let op = head s
                        (y,s2) = factor.getNum.tail $s
                        z = if op=='+' then x+y else x-y
                    in  expr (z,s2)
