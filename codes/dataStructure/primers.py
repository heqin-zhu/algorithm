def get(n)
    li = [i for i in range(2,n)]
        i = 1
        while  i <len(li):
            prod =2 * li[i] 
            while prod <=li[-1]:
                if prod in li:
                    li.remove(prod)
                prod+=li[i]
            i+=1
    return li