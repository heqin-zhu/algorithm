def permute(n):
    def _util(lst,i):
        if i==n:print(lst)
        else:
            for j in range(i,n):
                lst[i],lst[j]=lst[j],lst[i]
                _util(lst,i+1)
                lst[i],lst[j]=lst[j],lst[i]
    _util([i for i in range(n)],0)

if __name__=='__main__':
    permute(5)
