# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        bfs=[]
        q=[]
        q.append(root)
        
        while(len(q)!=0):
            
            lvl=[]
            
            for i in range(len(q)):
                
                v=q.pop(0)  #remove first element
                if v!=None:
                    
                    lvl.append(v.val)
                    q.append(v.left)
                    q.append(v.right)
                    
                   
                
            if lvl!=[]:
                bfs.append(lvl)
                
                
        return bfs
            
        
                
     
        