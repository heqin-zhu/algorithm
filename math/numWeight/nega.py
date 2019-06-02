def nega(n:int,base=-2:int)->:list:
    '''return list of num, the first is the highest digit'''
    if base>-2:
        raise Exception(f"[Error]: invalid base: {base}, base should be no more than -2")
    ans = []
    while n:
        k = n%base
        if k<0:
            k-=base
        ans.append(k)
        n = (n-k)//base
    return ans[::-1]
