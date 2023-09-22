# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
       
        #Iterative implementation 
        
       
        res = []
        stack = []
        if root:stack.append(root)
        
        while stack:
            
            node = stack.pop()
            
            res.append(node.val)
            
            if node.right:  stack.append(node.right)  #we append right to the stack
                                                 #first because it will be poped later
                                                
                    
            if node.left:   stack.append(node.left)
            
                
                
        return res
            