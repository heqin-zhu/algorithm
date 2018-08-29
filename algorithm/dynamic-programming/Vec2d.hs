module Vec2d
(Vec2d,
 getVal,
 setVal
 ) where
import Data.List (intercalate)

data Vec2d a = Vec (Int,Int) [a] | Vec2 [[a]]

instance (Show a)=>Show (Vec2d a) where
    show (Vec2 ll) = show2d ll
    show (Vec (x,y) lst) = show2d $ slice y lst

getVal i j (Vec (x,y) lst) = lst !! (i*y+j)
getVal i j (Vec2 ll) = ll !! i !! j

setVal val i j (Vec (x,y) lst) = 
    let pos = i*y+j
        before = take pos lst
        after  = drop (pos+1) lst
    in  Vec (x,y)  $before ++ [val] ++ after

setVAl val i j (Vec2 ll) = 
    let before =  take i ll
        origin =  ll !! i
        new    =  take j origin ++ [val] ++ drop (j+1) origin
        after  =  drop (i+1) ll
    in  Vec2 $before ++ [new] ++ after

show2d::(Show a)=>[[a]]->String
show2d  ll = 
        let str =concat . map (\lst-> show lst ++",\n") $ll      -- intercalate ",\n" . map show $ ll
        in  "Vector 2d: [\n"++str++ "]\n"

slice n lst
    | length lst <= n = [lst]
    | otherwise      = (take n lst) : (slice n  $drop n lst)
    
