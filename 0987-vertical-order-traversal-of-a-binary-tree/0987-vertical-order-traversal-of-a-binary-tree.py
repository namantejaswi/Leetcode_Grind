# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        dic=defaultdict(list)
        
        left_most=float("inf")
        right_most=float("-inf")
        
        def dfs(node,x,y):
            
            nonlocal left_most
            nonlocal right_most
            if not node:    return
            
            else:   
                left_most=min(left_most,x)
                right_most=max(right_most,x)
                dic[x].append((y,node.val))
                dfs(node.left,x-1,y+1)
                dfs(node.right,x+1,y+1)
                
        dfs(root,0,0)
                
        res=[]
        for x in range(left_most,right_most+1):
            
            col=[]
            for y,v in sorted(dic[x]):   
                col.append(v)          
                
            res.append(col)
                
        return res
            
          
        
        