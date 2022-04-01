# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
 
        def lca(node,p,q):
            
            if not(node): return
            
            if node.val==p.val or node.val==q.val:#we are told all values are unique
                return node
            
            l=None
            r=None
            
            if root.left!=None:
                l=lca(node.left,p,q)
                
            if root.right!=None:
                r=lca(node.right,p,q)
                
                
            if l!=None and r!=None: return node
                
                #if we find a node such that it has both l and r has a node return                   #value then that is the node
            
            
            else:
                return l or r   #we are garunteed if both p and q are present
                                #if we find one on one side or initial root the                                     #other value is definitely a decendent of it. 
                
        return lca(root,p,q)