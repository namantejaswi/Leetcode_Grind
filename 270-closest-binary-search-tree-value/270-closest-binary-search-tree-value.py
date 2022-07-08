# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        
        closest=root.val
        
        
        while root:
            
            if abs(root.val-target)<abs(target-closest):
                closest=root.val
                
            if root.val==target:
                return root.val
            
            elif target>root.val:
                root=root.right
                
            else:
                root=root.left
            
            
            
        return closest     
            
            
            
       