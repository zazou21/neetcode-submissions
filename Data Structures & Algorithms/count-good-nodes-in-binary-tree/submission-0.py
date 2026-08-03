# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxval):
            if node is None:
                return 0    
            result=1 if node.val>=maxval else 0
            new_max=max(maxval,node.val)
            result+=dfs(node.left,new_max)
            result+=dfs(node.right,new_max)
            return result
        
        return dfs(root,root.val)
        

        
