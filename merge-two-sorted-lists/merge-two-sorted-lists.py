# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode(0)
    
        l3=dummy
            
        while(l1 and l2):   #Checking neither is none
            
            if(l1.val<=l2.val):
                
                l3.next=l1
                l1=l1.next
                
            else:
                l3.next=l2
                l2=l2.next
            
            l3=l3.next
            
            
        if(l1 is None):
            l3.next=l2
        if(l2 is None):
            l3.next=l1
                
        return dummy.next
                
            
        