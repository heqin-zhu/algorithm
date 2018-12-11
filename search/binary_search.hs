search  i li= binary 0  $length li -1
             where binary a b= let mid = div (a+b) 2
                                   p = li!!mid 
                               in  if a>=b then a
                                   else if p==i then mid
                                   else if p>i then binary a $mid-1
                                   else   binary (mid+1) b
