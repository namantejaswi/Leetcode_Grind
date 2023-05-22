# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
    
        
        def traverse(node, left, right):
            nonlocal mx

            if node:                    
                mx =max(mx,left,right)

                traverse(node.left,0,left+1)   
                traverse(node.right,right+1,0)
            
    
        mx=0
        traverse(root,0,0)
        return mx
    
    

    
    
    
    
    