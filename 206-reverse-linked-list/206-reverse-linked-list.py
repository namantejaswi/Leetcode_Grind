# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def helper(head):
            
            
            if not head: return
            
            if   not head.next:
                return head
                
            else:
                forward=helper(head.next)
                head.next.next=head
                head.next=None
                return forward
        return helper(head)