# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res=0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        def depth(x):
            
            if x==None: return 0
            
            left = depth(x.left)
            right=depth(x.right)
            
            self.res = max(self.res, left+right)
            
            return 1 + max(left, right)
            
        depth(root)
        return self.res