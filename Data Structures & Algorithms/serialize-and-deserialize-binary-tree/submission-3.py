# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"
        serialized=[]
        queue=deque([root])
        while queue:
            node=queue.popleft()
            if not node:
                serialized.append("null")
            else:
                serialized.append(str(node.val))
                queue.append(node.left) 
                queue.append(node.right)
        return ",".join(serialized)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values=data.split(",")
        if values[0] == "null":
            return None
        root = TreeNode(int(values[0]))
        queue = deque([root])
        ptr=1
        while queue:
            node=queue.popleft()
            if values[ptr] != "null":
                node.left=TreeNode(int(values[ptr]))
                queue.append(node.left)
            ptr+=1
            if values[ptr] != "null":
                node.right=TreeNode(int(values[ptr]))
                queue.append(node.right)
            ptr+=1
        return root




