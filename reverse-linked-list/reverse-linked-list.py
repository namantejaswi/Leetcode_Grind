# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not head or not head.next:   return head
        
        
        else:
            res=self.reverseList(head.next)
            temp=head.next
            temp.next=head
            head.next=None
            return res
        
        