def permute(lst,n):
    ''' O(n!), optimal'''
    if n==1:print(lst)
    else:
        for i in range(n):
            lst[i],lst[n-1] = lst[n-1],lst[i]
            permute(lst,n-1)
            lst[i],lst[n-1] = lst[n-1],lst[i]

if __name__=='__main__':
    n = 3
    permute([i for i in range(n)],n)
