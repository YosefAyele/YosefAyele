class Node:
    def __init__(self,key,value):
        self.k=key
        self.val=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        
        self.cap=capacity
        self.cache={}   # maps a key to a node
        
        self.right= Node(0,0)
        self.left=Node(0,0)
        
        self.left.next, self.right.prev= self.right,self.left
    
    #remove from the left ....right after the left most dummy node
    def remove(self,node):
        prev, nxt= node.prev, node.next
        
        prev.next=nxt
        nxt.prev= prev
        
        
    #adds a node at the left...right before the rightmost dummy Node
    def add(self,node):
        prev, nxt= self.right.prev, self.right
        prev.next=node
        nxt.prev=node
        node.next=nxt
        node.prev=prev
    
        
    def get(self, key: int) -> int:
        
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.remove(self.cache[key])
            
        self.cache[key]=Node(key,value)
        self.add(self.cache[key])
        
        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            
            self.cache.pop(lru.k,lru.val)

            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)