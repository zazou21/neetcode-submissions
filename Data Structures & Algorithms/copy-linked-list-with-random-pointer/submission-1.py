"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map={}
        
        ptr=head
        while ptr:
            node_map[ptr]=Node(x=ptr.val)
            ptr=ptr.next
        ptr=head
        while ptr:
            node=node_map[ptr]
            node.next=node_map.get(ptr.next,None)
            node.random=node_map.get(ptr.random,None)
            ptr=ptr.next
        return node_map.get(head,None)
            
        


        