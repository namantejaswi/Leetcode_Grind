# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res=[] 
       
            
        def inorder(root):
            
            if(root):
                
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)

            return res
        
        ans= inorder(root)
        
        for i in range(len(ans)):
            if type(ans[i])!=int:
                ans.pop(i)
                
        print (ans)
        
        return(ans[k-1])