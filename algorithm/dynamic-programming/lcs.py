def lcs(a,b):
    '''time: O(mn); space: O(mn)'''
    m,n= len(a),len(b)
    board = [[[] for i in range(n+1)] for i in range(m+1)]
    for i in range(m):
        for j in range(n):
            if a[i]==b[j]:
                board[i+1][j+1] =board[i][j]+[a[i]]
            elif len(board[i][j+1]) < len(board[i+1][j]):
                board[i+1][j+1] = board[i+1][j]
            else :
                board[i+1][j+1] = board[i][1+j]
    return board[m][n]

def lcs2(a,b):
    '''time: O(mn); space: O(m)'''
    m,n= len(a),len(b)
    board = [[] for i in range(n+1)]
    for i in range(m):
        last = []
        for j in range(n):
            if a[i]==b[j]:
                board[j+1] =board[j]+[a[i]]
            elif len(board[j+1]) < len(last):
                board[j+1] = last
            last = board[j+1]
    return board[n]

if __name__ =='__main__':
    a="dsaffqewqfqewregqwefqwe"
    b="adsfsfs3qt5yhyh24efwq"
    print(lcs(a,b))
    print(lcs2(a,b))
