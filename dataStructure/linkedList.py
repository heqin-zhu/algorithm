class node:
    def __init__(self,val,follow=None):
        self.val = val
        self.follow = follow
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.tail = self.head = node(None)

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        nd = self.head
        for i in range(index+1):
            nd = nd.follow
            if nd is None:return -1
        return nd.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        nd = node(val,self.head.follow)
        self.head .follow = nd
        if self.tail.val is None:self.tail = nd
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.tail.follow = node(val)
        self.tail = self.tail.follow
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        nd = self.head
        for i in range(index):
            nd = nd.follow
            if nd is None:
                return
        new = node(val,nd.follow)
        nd.follow = new
        if self.tail == nd:
            self.tail = new
                

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        nd = self.head
        for i in range(index):
            nd = nd.follow
            if nd is None:return
        if self.tail == nd.follow:self.tail = nd            
        if nd.follow:nd.follow = nd.follow.follow
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
