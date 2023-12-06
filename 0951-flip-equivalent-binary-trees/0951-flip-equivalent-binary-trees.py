# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        
        def is_same(root1,root2):
            
    
            if not root1 and not root2: return True    
        
            if root1 and not root2 or root2 and not root1:  return False
             
            
            if root1.val!=root2.val:  return False
            
            
            if root1.val == root2.val:  
            
            #flip or no flip something must be true
            
                return (is_same(root1.left, root2.right)  and is_same(root1.right,root2.left)) or (is_same(root1.right, root2.right) and is_same(root1.left , root2.left))
        
        
        return is_same(root1,root2)