# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        h=head
        slowptr=head
        fastptr=head.next
        
        if not head or not head.next: return
        
        
        while(fastptr.next):
            
            if not fastptr.next.next:   
                
                fastptr=fastptr.next
                #slowptr=slowptr.next
                
            else:   
                
                fastptr=fastptr.next.next
                slowptr=slowptr.next
                
        temp=slowptr
        n2=temp.next.next
        slowptr.next=n2
        return h