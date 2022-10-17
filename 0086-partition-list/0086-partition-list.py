# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        
        lesser_ptr=ListNode()
        sent_l=lesser_ptr
        
        greater_ptr=ListNode()
        sent_g=greater_ptr
        
        while head:
            
            if head.val<x:
                lesser_ptr.next=head
                lesser_ptr=lesser_ptr.next
                
                
            else:
                
                greater_ptr.next=head
                greater_ptr=greater_ptr.next
                
            head=head.next        
                
        lesser_ptr.next=sent_g.next
        greater_ptr.next=None
        
        return sent_l.next
                
        
        