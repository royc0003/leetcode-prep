class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0) # left == least recently used, right = most recently used
        self.left.next, self.right.prev = self.right, self.left
        
        
    # remove from linkedList
    def remove(self, curNode):
        prevNode, nextNode = curNode.prev, curNode.next
        prevNode.next, nextNode.prev = nextNode, prevNode
    
    # insert to right
    def insert(self, curNode):
        leftNode, rightNode = self.right.prev, self.right
        leftNode.next, rightNode.prev = curNode, curNode
        curNode.next, curNode.prev = rightNode, leftNode
        
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        # create a new node and insert to chacheMap
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        # cache eviction policy happens here
        if len(self.cache) > self.capacity:
            # remove from LRU
            lru = self.left.next.key
            self.remove(self.cache[lru])
            del self.cache[lru]
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)