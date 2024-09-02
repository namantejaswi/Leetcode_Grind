# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        if not root:    return

        
        def dfs(node,p,q):
            
            if not node:    return None
            
            if  node.val == p.val or node.val == q.val:
                return node 
            
            
            left_sub_tree = None
            right_sub_tree = None
            
            
            if node.left:   left_sub_tree = dfs(node.left,p,q)
            if node.right:  right_sub_tree = dfs(node.right,p,q)
            
            #if in our post order traversal we get true from both lst and rst then we have found the lca, because we are following post order left right root then it means we wills always get the lca first
            
            #we hAVE NOW SEEN LST AND RST NOW WE CHECK IF GET EITHER ONE OR BOTH OF P AND Q IN OUR LST AND RST
            
            if left_sub_tree and right_sub_tree:
                return node
             
            elif left_sub_tree and not right_sub_tree:
                    return left_sub_tree
                
            elif right_sub_tree and not left_sub_tree:
                    return right_sub_tree
                    
            
        return dfs(root,p,q)