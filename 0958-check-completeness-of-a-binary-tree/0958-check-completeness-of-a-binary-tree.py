# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        
        
        # calulate the x cordinate of each of the nodes
        # if the tree is complete then the x cordinate of the last node should be 
        # equal to the number of nodes we set the left cordinate of a node to 2x and
        #right to 2x+1  and then we check if the last cordinate is equal to no of node
        
        
        #                       1
        #                      / \
        #                     2   3
        #                    / \  /
        #                   4   5 6    
        #
        
        
        mx=0
        count=0
        def count_cord(node,position):
            nonlocal mx,count
            if not node:
                return
            
            else:
                x=position
                count+=1
                mx=max(mx,position)
                
                count_cord(node.left,2*x)
                count_cord(node.right,(2*x)+1)
                
                
        count_cord(root,1)
        return mx==count