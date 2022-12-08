# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        l=[]
        def dfs(node):
            
            nonlocal l
            
            if not node:   return
            
            if not node.left and not node.right:
                l.append(node.val)
                return
            
            dfs(node.left)
            dfs(node.right)
            
            
        dfs(root1)
        l1=l
        l=[]
        dfs(root2)
        l2=l
        return l1==l2
        
            