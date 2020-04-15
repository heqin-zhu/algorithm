class unionFindSet:
    def __init__(self, S):
        self.S = {i: i for i in S}

    def find(self, x):
        if x != self.S[x]:
            self.S[x] = self.find(self.S[x])
        return self.S[x]

    def union(self, a, b, key=lambda x: x):
        x, y = sorted((self.find(a), self.find(b)), key=key)
        self.S[a] = self.S[b] = self.S[y] = x
