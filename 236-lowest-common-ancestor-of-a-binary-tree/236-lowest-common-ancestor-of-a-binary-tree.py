# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def lca(node,p,q):
            
            if not node: return

            if node.val==p.val or node.val==q.val:
                return node

            l=None
            r=None
            
            if node.left:
                l=lca(node.left,p,q)        #no return
                
            if node.right:
                r=lca(node.right,p,q)       #no return
                
                
            if l and r:    #return the first instance we have
                                             #both nodes
                return node
            
            #we found one of the node
            elif (l and not r): return l
            elif (r and not l): return r
             
            #because we aregarunteed that boththe ndes exist
        
        return lca(root,p,q)