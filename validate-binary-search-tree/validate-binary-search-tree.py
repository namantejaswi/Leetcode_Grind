# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        #Perform inorder traversal and check if they are sorted-----O(n)
        
        
        s=[]
        
        def inorder(root):
            
            if root:
                
                inorder(root.left)
                
                #print(root.val)
                
                s.append(root.val)
                
                inorder(root.right)
                
            return s
            
        r=inorder(root)
        print(r)
        
        flag=True
        for i in range (1,len(s)):
            
            if(s[i-1]<s[i]):
                pass
            else:
                flag=False
                
        return flag
            
                
                