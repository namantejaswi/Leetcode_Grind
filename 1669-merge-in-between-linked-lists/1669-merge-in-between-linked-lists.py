# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        
        #Traverse list 1 reach a th node store it continue and each bth node
        #now attach ath node.next to list 2 reach the end of list 2 and attach next to bth node
        
        node_A=ListNode()
        node_B=ListNode()
        
        h1=list1
        head=list1
        cnt=0
        while head:
            
            if cnt==a-1:  node_A=head
            
            elif cnt==b:    
                node_B=head.next
                h2=node_B
            cnt+=1
            head=head.next
                        
            
        print(node_A.val,node_B.val)
        
        
        node_A.next=list2
        
        h=list2
        while h.next:
            h=h.next
            
        h.next=node_B
        

        
        return h1