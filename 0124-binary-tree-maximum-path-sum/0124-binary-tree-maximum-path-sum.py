# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
    
    
    
        #kadane on trees
        
        #Brute force woul be n^2 for n nodes we enumerate all paths b/w 2 nodes

        mx = float("-inf")
        
        def subtree_sum(node):
            
            nonlocal mx
            
            if not node:return 0
            
            lst = max(subtree_sum(node.left),0)
            rst = max(subtree_sum(node.right),0)
            
            #incase one of them is -ve it is ignore by choosing 0
            
            mx = max(mx, lst+rst+node.val)
            
           
            #While going upsince we are choosing a path we cant have both lst andd rst, if we choose to continue to move upward for our path we choose the max of them an move up, also if the entere tree is the max path it would already reflext in mx 
            
            mx_choosing_one_going_up= max(lst,rst)+node.val
            return mx_choosing_one_going_up
        
        subtree_sum(root)
        return mx
        