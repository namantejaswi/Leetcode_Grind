# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        #level order traversal with alternating order of appending levels
        
    
        q=deque([root])
        #bfs_order=[]
        zig_zag=[]
        
        count=-1
        while q:
            
            levels=[]
            
            for i in range(len(q)):
                
                v=q.popleft()
                
                if v:
                    levels.append(v.val)
                    q.append(v.left)
                    q.append(v.right)
                    
                
            if levels:
                count+=1
                #bfs_order.append(levels) 
                if count%2==0:  
                    zig_zag.append(levels)
                else:  
                    levels.reverse()
                    zig_zag.append(levels)
                    
        #print(bfs_order)
        return zig_zag
            
        