# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def lca(node,p,q):
            
            #Base Case
            
            if node.val==p.val or node.val==q.val:
                
                print(node.val)
                return node
            
            #Recursive case
            
            if node.val>p.val and node.val>q.val:
                return lca(node.left,p,q)
                
            if node.val<p.val and node.val<q.val:
                return lca(node.right,p,q)
                
            else:   return node
            
            
        return lca(root,p,q)