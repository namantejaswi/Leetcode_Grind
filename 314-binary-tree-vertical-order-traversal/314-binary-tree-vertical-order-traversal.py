# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        column_elements={}
        
        q=deque([(root,0)])     #root is at zero index of col left -ve right +ve
        
        
        while q:
            
            node,col_idx=q.popleft()
            
            if node:
                
                if col_idx in column_elements:
                    column_elements[col_idx].append(node.val)
                    
                else:   column_elements[col_idx]=[node.val]
                    
                
                q.append([node.left,col_idx-1])
                q.append([node.right,col_idx+1])
                
                
        res=[]
        d=dict(sorted(column_elements.items(), key=lambda x:x[0]))
          
        for v in d.values():
            res.append(v)
            
        return res
            
        

            
            
            
            
                
                
    