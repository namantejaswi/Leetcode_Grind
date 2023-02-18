# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def helper(node):
        
            if not node:    return  

            rst = helper(node.right)
            lst = helper(node.left)
            

            node.left = rst
            node.right = lst
            
            return node

        return helper(root)
     
        
        
        
    