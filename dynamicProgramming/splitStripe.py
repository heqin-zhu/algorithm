''' mbinary
#########################################################################
# File : splitStripe.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-08-24  17:07
# Description:
#########################################################################
'''

'''
    There is stripe which length is n, 
    priceMap contains a map for different length of stripe and its price
    then find the maximum price to split the stripe in different shorter stripes
    ( including  the original length if possible)
'''
    
def count(n,prices):
    def best(cur): 
        # note that copying the list or create a new list in the following new_stripes codes
        if cur in values: return values[cur],stripes[cur] 
        maxPrice = 0
        new_stripes=[]
        for i,j in prices.items():
            if i<=cur: 
                p, tmp = best(cur-i)
                if maxPrice<p+j:
                    new_stripes = tmp+[i]  # if the list is not copyed, create a new list, don't use append
                    maxPrice =p+j
        values[cur] = maxPrice
        stripes[cur] = new_stripes
        return maxPrice,new_stripes
    values = {0:0}
    stripes = {0:[]}
    return best(n)



if __name__=='__main__':
    li = [(1,1),(2,5),(3,8),(4,9),(5,10),(6,17),(7,17),(8,20),(9,24),(10,30)]
    prices = {i:j for i,j in li}
    n = 40

    d = {i:count(i,prices) for i in range(n+1)}
    for i in range(n+1):
        print(i,d[i])
