# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        sentinel=ListNode(0)
        sentinel.next=head
        prev=sentinel
        
        while(head):
            
            #if the next value is same do not set previous to it
            if head.next and head.val==head.next.val:
                
                #reach the end of duplicate values
                while(head.next and head.val==head.next.val):
                    
                    head=head.next
                    
                #once we reach the end set the next to prev.next   
                prev.next=head.next
                
                
            else: prev=prev.next
                
            head=head.next
            
            
        return sentinel.next
            
            