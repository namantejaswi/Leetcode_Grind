# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        #Iterative
        
        stack = []
        
        res = []
        
        while root or stack:
            
            if root:
                stack.append(root)
                root=root.left
                
            else:
                
                popped_node = stack.pop()
                res.append(popped_node.val)
                root = popped_node.right
                
                
        return res
                
        
        