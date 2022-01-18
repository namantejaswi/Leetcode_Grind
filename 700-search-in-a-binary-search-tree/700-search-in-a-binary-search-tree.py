# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        #poor wording smh just need to return the node we find
        
        def helper(node,val):
            
            if not node:    return
            
            if node.val==val:    return node
            
            if node.val>val:    return helper(node.left,val)
            
            if node.val<val:    return helper(node.right,val)
            
            
        return helper(root,val)
            
        
        return helper(root,val)