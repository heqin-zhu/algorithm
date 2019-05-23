''' mbinary
#########################################################################
# File : allOne.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-05-19  23:07
# Description:
#########################################################################
'''


class node:
    def __init__(self, val=None, keys=None, pre=None, next=None):
        self.val = val
        self.keys = set() if keys is None else keys
        self.pre = pre
        self.next = next

    def __lt__(self, nd):
        return self.val < nd.val


    def __contains__(self, k):
        return k in self.keys

    def __bool__(self):
        return len(self.keys) != 0

    def __repr__(self):
        return 'node({},{})'.format(self.val, self.keys)
    def addKey(self, key):
        self.keys.add(key)


    def remove(self, key):
        self.keys.remove(key)

    def getOneKey(self):
        if self:
            key = self.keys.pop()
            self.keys.add(key)
            return key
        return None


class allOne:
    def __init__(self):
        self.head = self.tail = node(0)
        self.head.next = self.head
        self.head.pre = self.head
        self.val_node = {0: self.head}
        self.key_value = {}

    def __str__(self):
        li = list(self.val_node.values())
        li = [str(i) for i in li]
        return  'min:{}, max:{}\n'.format(self.head.val,self.tail.val)   \
                + '\n'.join(li)
    def __contains__(self,k):
        return k in self.key_value

    def getMaxKey(self):
        return self.tail.getOneKey()

    def getMinKey(self):
        return self.head.getOneKey()

    def getMaxVal(self):
        k = self.getMaxKey()
        if k is not None:
            return self.key_value[k]

    def getMinVal(self):
        k = self.getMinKey()
        if k is not None:
            return self.key_value[k]

    def addIncNode(self, val):
        # when adding a node,inc 1, so it's guranted that node(val-1)  exists
        self.val_node[val] = node(val)
        self.val_node[val].pre = self.val_node[val - 1]
        self.val_node[val].next = self.val_node[val - 1].next
        self.val_node[val - 1].next.pre = self.val_node[
                                                        val - 1].next = self.val_node[val]
        if self.tail.val < val:
            self.tail = self.val_node[val]
        if self.head.val > val or self.head.val == 0:
            self.head = self.val_node[val]

    def addDecNode(self, val):
        # when adding a node,dec 1, so it's guranted that node(val+1)  exists
        self.val_node[val] = node(val)
        self.val_node[val].next = self.val_node[val + 1]
        self.val_node[val].pre = self.val_node[val + 1].pre
        self.val_node[val + 1].pre.next = self.val_node[
                                                        val + 1].pre = self.val_node[val]
        if self.head.val > val:
            self.head = self.val_node[val]

    def delNode(self, val):
        self.val_node[val].next.pre = self.val_node[val].pre
        self.val_node[val].pre.next = self.val_node[val].next
        if self.tail.val == val: self.tail = self.val_node[val].pre
        if self.head.val == val: self.head = self.val_node[val].next
        del self.val_node[val]

    def inc(self, key):
        ''' inc key to value val'''
        val = 1
        if key in self.key_value:
            val += self.key_value[key]
        self.key_value[key] = val
        if val not in self.val_node:
            self.addIncNode(val)
        self.val_node[val].addKey(key)
        if val != 1:  # key in the pre node
            preVal = val - 1
            nd = self.val_node[preVal]
            if key in nd:
                nd.remove(key)
                if not nd:
                    self.delNode(preVal)

    def dec(self, key):
        if key in self.key_value:
            self.key_value[key] -= 1
            val = self.key_value[key]
            if val == 0:
                del self.key_value[key]
            elif val>0:
                if val not in self.val_node:
                    self.addDecNode(val)
                # notice that the headnode(0) shouldn't add key
                self.val_node[val].addKey(key)
            nextVal = val + 1
            nd = self.val_node[nextVal]
            if key in nd:
                nd.remove(key)
                if not nd:
                    self.delNode(nextVal)

    def delMinKey(self):
        key = self.getMinKey()
        if key is not None:
            val = self.key_value.pop(key)
            nd = self.val_node[val]
            nd.remove(key)
            if not nd:
                self.delNode(val)
        return key
    def append(self,key):
        if key in self.key_value:
            raise Exception(f'[Error]: key "{key}" exists')
        if self.key_value:
            val = self.key_value[self.getMaxKey()]
            self.key_value[key] = val
            self.val_node[val].addKey(key)
        self.inc(key)
    def move_to_end(self,key):
        val = self.key_value.pop(key)
        nd = self.val_node[val]
        nd.remove(key)
        if not nd:
            self.delNode(val)
        self.append(key)



if __name__ == '__main__':
    ops = [
           "inc", "inc", "inc", "inc", "inc", "dec", "dec", "getMaxKey",
           "getMinKey",'dec'
          ]
    obj = allOne()
    data = [["a"], ["b"], ["b"], ["b"], ["b"], ["b"], ["b"], [], [],['a']]
    operate = {
               "inc": obj.inc,
               "dec": obj.dec,
               "getMaxKey": obj.getMaxKey,
               "getMinKey": obj.getMinKey
              }
    for op, datum in zip(ops, data):
        print(f'{op}({datum}): {operate[op](*datum)}')
        print(obj)
        print()
