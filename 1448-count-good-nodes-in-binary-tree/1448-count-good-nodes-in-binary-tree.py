# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        total_good_nodes=0
        
        def countnode(curr_node:TreeNode, mx_so_far)->None:
            
                         
            nonlocal total_good_nodes
            
            
            if mx_so_far<=curr_node.val:
                total_good_nodes+=1
                
            
            if curr_node.right:
                
                countnode(curr_node.right,max(curr_node.val,mx_so_far))
                
            if curr_node.left:
                
                countnode(curr_node.left,max(curr_node.val,mx_so_far))
                
                
        countnode(root,-10**5)
        
        return total_good_nodes