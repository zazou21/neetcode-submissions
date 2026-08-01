# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        results=[]
        queue.append(root)
        while queue:
            length=len(queue)
            level_vals=[]
            for i in range(length):
                node=queue.popleft()
                if node:
                    level_vals.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level_vals:
                    results.append(level_vals)
        return results
        

    



        
        