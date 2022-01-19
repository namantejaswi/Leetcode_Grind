# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
       
        s=targetSum
        
        def helper(node,s):
            
            if not node:    return False
                        
            else:
                
                s=s-node.val
                
                if not node.left and not node.right:    #not a leaf
                    if s==0:    return True
                    else:   return False
                    
                return helper(node.left,s) or helper(node.right,s)
            
            
        return helper(root,targetSum)
            