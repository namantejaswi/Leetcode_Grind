# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
       
        curr =head
        prev =None
        
        while curr.next:
            
            if curr.val>curr.next.val:
                #then move curr.next to start
                
                negative = curr.next
                curr.next=curr.next.next
                negative.next = head
                head = negative
                
            else:   curr= curr.next
                
                
        return head
                
                
            
                
                
                
                