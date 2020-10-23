class DoubleList:
    def __init__(self, val=None):
        self.val = val
        self.next = self
        self.prev = self
        
    def __str__(self):
        return "PRINT {}".format(self.val)

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.n = 0
        self.d = {}
        self.head = DoubleList()
        
    def addNode(self, node):
        old = self.head.next
        
        old.prev = node
        self.head.next = node
        
        node.next = old
        node.prev = self.head
        
    def removeNode(self, node):
        prev = node.prev
        nxt = node.next
        
        prev.next = nxt
        nxt.prev = prev
        
    def evictNode(self):
        tail = self.head.prev
        self.removeNode(tail)
        
        return tail
        

    # @return an integer
    def get(self, key):
        if key in self.d:
            node = self.d[key][1]
            self.removeNode(node)
            self.addNode(node)
            return self.d[key][0]
        
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.d:
            node = self.d[key][1]
            self.removeNode(node)
            self.addNode(node)
            self.d[key] = (value, node)
            return
        
        if self.n == self.capacity:
            node = self.evictNode()
            del self.d[node.val]
            self.n -= 1
            
        self.n += 1
        node = DoubleList(key)
        self.addNode(node)
        
        self.d[key] = (value, node)
            
        
