# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        def helper(head):
            
            if not head or (not head.next):
                return head
            
            
            else:
                

                first=head
                second=head.next
                
                head.next=helper(second.next)
                
                second.next=head 
                
            return second
        
        
        return helper(head)
                
        