# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        mx = 0
        
        def dfs(node,parent_val):
            
            if not node:    return 0
            
            nonlocal mx
            
            
            left = dfs(node.left,node.val)
            right = dfs(node.right,node.val)
            
            mx = max(mx,left+right)
            
            if node.val==parent_val:
                return 1 +max(left,right)
            
            else:   return 0
            
        dfs(root,None)
        return mx