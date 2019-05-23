from allOne import  allOne

'''In this implementation, the lru doesn't use some funcs of allOne,
    such as dec,addDecNode
'''
class lru:
    def __init__(self, capacity):
        self.capacity = capacity
        self.allOne = allOne()
        self.data = {}
    def get(self,key):
        if key in self.data:
            self.allOne.move_to_end(key)
            return self.data[key]
        return -1
    def put(self,key,value):
        if key not in self.data:
            if len(self.data)==self.capacity:
                k = self.allOne.delMinKey()
                if k in self.data:
                    del self.data[k]
            self.data[key]=value
            self.allOne.append(key)
        else:
            self.data[key]=value
            self.allOne.move_to_end(key)


if __name__ == '__main__':
    ops = ["put","put","get","put","get","put","get","get","get"]
    data = [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    obj = lru(2)
    operate = {'get':obj.get,'put':obj.put}
    for op, args in zip(ops,data):
        print(f'{op}({args}): {operate[op](*args)}\n{obj.data}\n')

