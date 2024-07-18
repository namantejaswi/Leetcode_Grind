# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        #An in order traversal of the bst will always be sorted
        
        if not root:    return True
        
        in_order = []
        
        def dfs(node):
            
            if node:
                
                #if in_order and in_order[-1]>node.val:  return False
                
                dfs(node.left)

                in_order.append(node.val)
                    
                dfs(node.right)
                
        dfs(root)
                
        for i in range(1,len(in_order)): 
            if in_order[i]<=in_order[i-1]:   return False

        return True