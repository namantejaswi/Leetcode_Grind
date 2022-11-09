# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res=[]
        
        def root_to_path(node,path):
            
            if not node:    return            
            else:
                if not node.left and not node.right:
                    path+=str(node.val)
                    res.append(path)
                    
                else:
                    root_to_path(node.left,path+str(node.val)+'->')
                    root_to_path(node.right,path+str(node.val)+'->')
          
        root_to_path(root,'')

        return res
                    