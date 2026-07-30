# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equalTree(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val!=q.val:
                return False
            left=equalTree(p.left,q.left)
            right=equalTree(p.right,q.right)
            return left and right
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        containsSubTree=equalTree(root,subRoot)
        if containsSubTree:
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
       
                



        