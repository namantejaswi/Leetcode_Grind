# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        slow=head
        fast=head
        
        
        while(fast and fast.next and fast.next.next ):
            slow=slow.next
            fast=fast.next.next
            
        #odd number of nodes
        if not fast.next:  
            return slow
        
        #even number of nodes
        return slow.next
            