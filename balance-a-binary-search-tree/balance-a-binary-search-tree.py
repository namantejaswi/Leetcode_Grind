# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
         
        res=[]
        def inorder(node):
            if node==None:
                
                return 
            
            else:
            
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)
        (inorder(root))   
        
        print(res)
        def create_bst(res):
            
            if not res:
                return None
            
            else:
                
                mid=len(res)//2
                
                root=TreeNode(res[mid])     #Need to convert int val to node
                root.left=create_bst(res[:mid])
                root.right=create_bst(res[mid+1:]) #mid included,start from mid+1
                
    
                return root
            
        return(create_bst(res))
            
            
            
            
            
            
    