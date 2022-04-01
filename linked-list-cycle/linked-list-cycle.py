# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        slowptr=head
        fastptr=head
        
        if not(head) or head.next==None:    return False
        
        while slowptr.next and fastptr.next :
            
            slowptr=slowptr.next
            if not(fastptr.next.next): return False
            fastptr=fastptr.next.next
            
            if slowptr==fastptr:    return True
            
        return False
            