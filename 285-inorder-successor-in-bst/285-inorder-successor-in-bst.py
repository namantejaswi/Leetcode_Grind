# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        
        
        res=[]
        
        def inorder(node):
            
            if not node:    return
            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
            
        inorder(root)
        
        if (res[-1]==p.val):   return None
            
        for i in range(0,len(res)-1):
            if res[i]==p.val:
                return(TreeNode(res[i+1]))
            