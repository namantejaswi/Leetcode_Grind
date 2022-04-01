# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        s=0
        def inorder_sum(node,l,h):
            nonlocal s
            if not(node):
                return
            
            
            inorder_sum(node.left,l,h)

            if node.val>=low and node.val<=high:
                s+=node.val
             
            inorder_sum(node.right,l,h)
                    
        inorder_sum(root,low,high)
        
        return s
                
            