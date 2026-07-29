# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxHeightSub(root):
            if root is None:
                return 0 
            return max(maxHeightSub(root.left),maxHeightSub(root.right)) + 1 
        if root is None:
            return True
        left=maxHeightSub(root.left) 
        right=maxHeightSub(root.right) 
        if abs(right-left) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
            




        