from colectons import deque
isVisted = [0]*362880
fac = [1,2,6,24,120,720,5040,40320]
lf = len(fac)
x= '9'
def cantor(s):
    sum = 0
    ls = len(s) 
    for i in range(ls):
        count = 0
        for j in range(i+1;ls):
            if s[i] > s[j]: count +=1
        sum += count*fac[lf-i-1]
    return sum

que = deque() 
class state: 
    def __init__(self,s,p,step=0,last=0):
        self.x = p
        self.s = list(s) 
        self.step = step
        self.path = []
        self.last = last
    def move(self):
        dir = [-3:'u',1:'r',3:'d',-1:'l']
        if self.last in dir :
            del dir[-self.last]
        if self.x<3:
            del dir[-3]
        if self.x>5:
            del dir[3]
        if self.x%3 is 0:
            del dir[-1]
        if self.x%3 is 2:
            del dir[1]
        for i in dir.keys():
            s = list(self.s)
            tmp = self.x + i
            s[self.x] = s[tmp]
            s[tmp] = x
            if not isVisted[cantor(s)]:
                new = state(s,tmp,self.step +1,i)
                new.path = self.path + [dir[i]]
                que.append(new)

def getPath(s):
    index = s.find('x')
    s =list(s)
    s[index] = '9'
    que.append(state(s,index,0,0))
    while que != deque():
        cur = que.popleft()
        ct = cantor(cur.s)
        if ct is 362879:
            return cur.path
        isVisted[] = 1
        cur.move()

if __name__ == '__main__':
    s=input()
    print(''.join(getPath(s)))
