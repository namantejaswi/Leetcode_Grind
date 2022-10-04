# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res=[]
        
        def calc_sum(node,curr_sum,arr):
            
            if not node: return
            curr_sum-=node.val
            
            if not node.left and not node.right and curr_sum==0: 
                #print("found 1",node.val)
                arr=arr+[node.val]
                res.append(arr)
                return 
                
            calc_sum(node.left,curr_sum,arr+[node.val])
            calc_sum(node.right,curr_sum,arr+[node.val])
                                   
                        
        calc_sum(root,targetSum,[])
        return res