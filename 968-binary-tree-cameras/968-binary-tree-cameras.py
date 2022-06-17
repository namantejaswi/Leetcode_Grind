# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        
        cnt=0
        
       
        def dfs(root):
            nonlocal cnt
            if not root:    return "covered by its child"
            
            l=dfs(root.right)
            r=dfs(root.left)
        
            if l=="need to be covered" or r=="need to be covered":
                cnt+=1
                return "child now has camera"
    
    
            if l=="child now has camera" or r=="child now has camera":
            
                return "covered by child"
            
            return "need to be covered"
        
            
        if dfs(root)=="need to be covered":
            return cnt+1
        else: return cnt
    
    
    