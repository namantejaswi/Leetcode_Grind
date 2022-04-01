# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        res=[]
        def pre_order(node):
            if not node:
                return  
            else:
                res.append(node.val)
                pre_order(node.left)
                pre_order(node.right)
                
        pre_order(root)       
                
        if(len(res)==0):
            return
        
        elif(len(res)==1):
            return(root)
        
        dummy=TreeNode(res[1])
        root.right=dummy
        root.left=None
        
        for i in range(2,len(res)):
            dummy.right=TreeNode(res[i])
            dummy=dummy.right
       