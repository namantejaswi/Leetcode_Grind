# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        res=[]
        
        def dfs(root):
            nonlocal res
            
            if not root:    return 
            
                  
            if root.left and root.right:   
                dfs(root.right)
                dfs(root.left)
            
            
            elif root.left and not root.right:
                res.append(root.left.val)
                dfs(root.left)
                
            elif root.right and not root.left:
                res.append(root.right.val)
                dfs(root.right)
                
          
                
        dfs(root)
        
        return res
                
            
                
        