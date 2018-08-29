import Vec2d
main = do
    let d=[1..10]
        ll = [[(i,j)| i<-[1..5]] | j<-['a'..'g']]
    print (Vec (2,5) d)
    print (Vec (5,2) d)
    print (Vec2 ll)
