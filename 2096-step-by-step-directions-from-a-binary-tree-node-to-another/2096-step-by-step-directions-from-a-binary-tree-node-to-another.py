# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        
        
        def lca(node):
            
            if not node:    return 
            
            if node.val==startValue or node.val==destValue:
                return node
            
            else:
                
                lst=lca(node.left)
                rst=lca(node.right)
                
                if lst and rst: return node
                
                else:   return rst or lst
                
        start=lca(root)        
        
#         def find_path(node,value,path)->str:
            
#             if not node:    return""
            
#             if node.val==value:
#                 return path
            
#             a=find_path(node.left,value,path+"L")
#             b=find_path(node.right,value,path+"R")
            
#             return a+b
            
            
#         p1=find_path(start,startValue,"")
#         p2=find_path(start,destValue,"")
        
                    
#         p1=p1[::-1]
            
#         res=""
        
#         for i in range(len(p1)):
            
#             if p1[i]=="L" or"R":  res+="U"
                
#         return res+p2
            
        p1 = p2 = ""
        stack = [(start, "")]
        while stack: 
            node, path = stack.pop()
            if node.val == startValue: p1 = path 
            if node.val == destValue: p2 = path
            if node.left: stack.append((node.left, path + "L"))
            if node.right: stack.append((node.right, path + "R"))
        return "U"*len(p1) + p2
        
        
                
            
            