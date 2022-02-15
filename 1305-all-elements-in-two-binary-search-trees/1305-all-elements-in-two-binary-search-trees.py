# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        
        list1=[]
        list2=[]
        def inorder(node,l):
            
            if not node:    return
            inorder(node.left,l)
            l.append(node.val)
            inorder(node.right,l)
            
        inorder(root1,list1)
        inorder(root2,list2)            
        
        #print(list1,list2)
        
        ptr1=0
        ptr2=0
        list3=[]
        
        while(ptr1<len(list1) and ptr2<len(list2)):
            
            if list1[ptr1]<=list2[ptr2]:
                list3.append(list1[ptr1])
                
                ptr1+=1
            else:   
                list3.append(list2[ptr2])
                
                ptr2+=1
        
        #print(ptr1,ptr2,list3)
        if ptr1==len(list1):
            list3[ptr1+ptr2:]=list2[ptr2:]
            
        elif ptr2==len(list2):
            list3[ptr1+ptr2:]=list1[ptr1:]
            
            
        return(list3)
        