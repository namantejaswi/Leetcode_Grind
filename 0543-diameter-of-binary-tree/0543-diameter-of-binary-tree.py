# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        dia = 0
        
        def dfs(node):
            nonlocal dia
            if not node:
                return 0 
            
            left_path = dfs(node.left)
            right_path = dfs(node.right)
            
        
            dia = max(dia,left_path+right_path)
            
            return 1+max(left_path,right_path)    
        
        dfs(root)
        return dia
            