# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        r=TreeNode(0)
        z=r
        r.left=root
        
        def helper(node,level):
            
            
            if not node:    return
            
            
            if node:
                #print(level,node.val)
                
                level+=1
                
                if level==depth+1:
                    if node.right:
                        
                        temp_node_1=node.right
                        node.right=None
                        node.right=TreeNode(val)
                        node.right.right=temp_node_1
                    
                    elif not node.right:
                        node.right=TreeNode(val)
                        
                    if node.left:
                        
                        temp_node_2=node.left
                        node.left=None
                        node.left=TreeNode(val)
                        node.left.left=temp_node_2
                        
                        
                    elif not node.left:
                        node.left=TreeNode(val)
                        
                        
                else: 
                    helper(node.right,level)
                    helper(node.left,level)    
                        
                    
            
        helper(r,1)
        return z.left
            
            
            
        