class LRUCache:

    class Node:
        def __init__(self,key,val):
            self.key=key
            self.val=val
            self.next=self.prev=None
            
    def __init__(self, capacity: int):
        self.left=self.Node(0,0)
        self.right=self.Node(0,0)
        self.cache={}
        self.capacity=capacity
        self.left.next=self.right
        self.right.prev=self.left
        
    def remove(self,node: Node):
        left=node.prev
        right=node.next
        left.next=node.next
        right.prev=node.prev

    def insert(self,node: Node):
        right=self.right
        left=self.right.prev
        right.prev=node
        left.next=node
        node.prev=left
        node.next=right
        


    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        mru=self.Node(key,value)
        self.insert(mru)
        self.cache[key]=mru
        if len(self.cache) > self.capacity:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)
        


        
        
        
