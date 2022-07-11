# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        
        res=0
        def dfs(root,n):
            nonlocal res
            
            
            if not root:    return
            elif root:
                
                n = (n*10) + root.val
                
            if not root.right and not root.left:
                #i.e leaf
                res+=n
            dfs(root.right,n)
            dfs(root.left,n)
                
        dfs(root,0)
        
        return res