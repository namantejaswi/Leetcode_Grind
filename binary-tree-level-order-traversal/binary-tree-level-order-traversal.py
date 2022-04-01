# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
    
        #Level order traversal is nothing but breadth first search 
             
        res=[]           
        q=[]
        q.append(root)

        while(len(q)!=0):
            
            level=[]
            
            for i in range(len(q)):
                
                v=q.pop(0)
                if v!=None:    
                    level.append(v.val)
                    q.append(v.left)
                    q.append(v.right)
                
            if level!=[]:
                res.append(level)
    
        return res