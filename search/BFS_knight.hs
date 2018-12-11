{- mbinary
#########################################################################
# File : BFS_knight.hs
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-11-11  19:40
# Description: 
#########################################################################
-}
{-
Given two different positions on a chess board, find the least number of moves it would take a knight to get from one to the other. The positions will be passed as two arguments in algebraic notation. For example, knight("a3", "b5") should return 1.

The knight is not allowed to move off the board. The board is 8x8.
-}

module ShortestKnightPath.Kata (knight) where
import Data.Char
import Data.List
knight :: String -> String -> Int
knight s1 s2  = let begin = axis s1
                    end =  axis s2
                    notEnd = all (\tp->tp /=end) 
                in length . takeWhile notEnd .iterate gen $[begin]

gen li = nub. flatten $map (filter  (\(a,b) ->a>0 && b>0 &&a<9&&b<9 ) . change)  li
change (a,b) = [(a-1,b-2),(a-1,b+2),(a+1,b-2),(a+1,b+2),(a+2,b-1),(a+2,b+1),(a-2,b+1),(a-2,b-1)]

axis s = (ord (s!!0) -96, digitToInt (s!!1)::Int)

flatten [] = []
flatten (x:xs) = x ++ flatten xs

