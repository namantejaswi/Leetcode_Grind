# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        
        
        q = deque([root])
        
        res=[]
        
        lvl=0
        
        while q:
            
            row=[]
            
            for i in range(len(q)):
                node= q.popleft()

                if node:    
                    row.append(node.val)
                    q.append(node.left)
                    q.append(node.right)


            if row:
                if lvl%2==0:  

                    res.append(row)
                else:   res.append(row[::-1])    

                lvl+=1

        return res
                    
                    