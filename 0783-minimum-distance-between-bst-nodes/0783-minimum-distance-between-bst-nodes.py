# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        mi=float('inf')
        res=[]
        
        def inorder(node):
            nonlocal res,mi
            
            if not node: return
        
        
            else:   
                
                
                inorder(node.left)
                if res: mi =min(mi,node.val-res[-1])
                res.append(node.val)
                
                inorder(node.right)
                
                
        
        inorder(root)
        print(res)
        return mi