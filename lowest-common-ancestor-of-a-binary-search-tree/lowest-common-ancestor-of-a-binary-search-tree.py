# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        
        def lca(node,p,q):
            
            if node.val>p.val and node.val>q.val: #if root is greater than both
                return lca(node.left,p,q)                #we check left sub tree 
                
            #same as node.val>max(p1.val,p2.val)
            
            elif node.val<p.val and node.val<q.val: #if root is less than both
                return lca(node.right,p,q)                  #we check right sub tree

            #we can also right it as node.val<=(max(p1.val,p2.val))
            else:
                return (node)
              
        return lca(root,p,q)
            