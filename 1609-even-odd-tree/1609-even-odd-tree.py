# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        if root.val%2==0:   return False
    
        
        q=deque([root])
        
        res = []
        while q:
            
            lvl = []
            
            for i in range(len(q)):
                
                node = q.popleft()
                
                lvl.append(node.val)
                if node.left:   q.append(node.left)
                    
                if node.right:  q.append(node.right)
                
         
            #print(lvl)
            res.append(lvl)
               
        #print(res)
        #we can reduce axuilary space to O(width) or O(2*height) or O(logn) by checking each level as we generate it it and it would also help us return early
        
        
        idx=0
        for nums in res:
              
                if idx%2==0:
                    if nums[0]%2==0:    return False
                    for i in range(1,len(nums)):
                        
                        if nums[i]<=nums[i-1] or nums[i]%2==0:
                            return False
                        
                elif idx%2==1:
                    if nums[0]%2!=0:    return False
                    for i in range(1,len(nums)):
                        
                        if nums[i]>=nums[i-1] or nums[i]%2==1:
                            return False
                idx+=1         
        
        return True            
                    
