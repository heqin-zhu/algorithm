genPrimes 2= [2]
genPrimes n = let li = genPrimes $n-1
in  if all (\x-> mod n x /=0) li then n:li else li
