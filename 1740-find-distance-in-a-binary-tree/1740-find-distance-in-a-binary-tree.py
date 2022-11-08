# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        
        
        def find_node(node,target,path):
            
            if not node:
                return ''
            if node.val==target:
                return path
            
            a = find_node(node.left,target,path+"L")
            b = find_node(node.right,target,path+"R")     
            
            return a+b
                    
                
                
                    
        path_of_p=(find_node(root,p,""))
        path_of_q=(find_node(root,q,""))
        
        
        
        lcp_len=0
        
        
        for i in range(min(len(path_of_p),len(path_of_q))):
            
            if path_of_p[i]==path_of_q[i]:  lcp_len+=1
                       
            else:   break
                       
        
        #print('p',path_of_p)
        #print('q',path_of_q)
        
        
        if lcp_len!=0: return len(path_of_p)+len(path_of_q)-2*lcp_len
        
        else:   return len(path_of_p)+len(path_of_q)
        
        
                       
                       
        
                    