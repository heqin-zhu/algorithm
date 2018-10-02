import qualified Data.Map  as M

{-
count function:
There is stripe which length is n, 
priceMap contains a map for different length of stripe and its price
then find the maximum price to split the stripe in different shorter stripes
( including  the original length if possible)
-}

priceMap  = M.fromList [(1,1),(2,5),(3,8),(4,9),(5,10),(6,17),(7,17),(8,20),(9,24),(10,30)]

count n priceMap =  _count 1 $M.fromList [(0,0)]
    where 
        end = n+1
        _count cur rst 
            | cur == end = rst
            | otherwise = _count (1+cur) (M.insert cur price rst)
                                where
                                    newRst = M.insert cur (getValue cur priceMap) rst 
                                    price = maximum. map getPrice $[0..div cur 2]
                                    getPrice a = (getValue a newRst ) + (getValue (cur-a) newRst)
                                    getValue key mp 
                                            | M.member key mp = mp M.! key
                                            | otherwise       = 0
