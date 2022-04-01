# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res=[]  
        def inorder(node): 
            if(node==None): return 
            
            else:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)
                
                
        inorder(root)   
        
        print(res)
        
        
        def val_to_swap(res):
            x=y=None
            
            for i in range(0,len(res)-1):
            
                if(res[i+1]<res[i]):
                
                    x=res[i+1]
                    i1=i+1
                        
                    if(y==None):
                        y=res[i]
                        i2=i
            print("values swaped",x,y)    

            return x,y      
        print(res)
        
        x,y=val_to_swap(res)
        
        def traverse(root):
            
            
            if root is not None:
                
                if root.val==x:
                    print("the val of root is",root.val)
                    root.val=y
                    print("changing the val of root to ",root.val)
                elif root.val==y:
                    print("the val of root is",root.val)
                    root.val=x
                    print("changing the val of root to ",root.val)
                
                traverse(root.left)
            
                traverse(root.right)
                              
        traverse(root)
        
        
        