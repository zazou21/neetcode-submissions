# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def heightSubTree(root):
            if root is None:
                return 0
            return(max(heightSubTree(root.left)+1,heightSubTree(root.right)+1))
        if root is None:
            return 0
        heightLeft=heightSubTree(root.left)
        heightRight=heightSubTree(root.right)
        sub = max(self.diameterOfBinaryTree(root.left),
                  self.diameterOfBinaryTree(root.right))

        return max(heightLeft+heightRight,sub)


          
        

        

        