# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    
        def helper(node):
            
            if not node:return 0
            
            else:
                
                left_max_height=helper(node.left)
                right_max_height=helper(node.right)
                
                return 1+max(left_max_height,right_max_height)
            
        return helper(root)