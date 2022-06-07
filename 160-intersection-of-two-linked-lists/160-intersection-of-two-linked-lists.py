# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        
        ptrA = headA
        ptrB = headB

        #in order to make sure moth ptrs of the 2 list travel the same distacne
        #once we reach the end of list b we move the pointer to the starting of the next list
        #this is same as calculating the length of the 2 lists and moving the head ptr of the larger list by the difference in the list before starting
        while ptrA != ptrB:
            
            if ptrA is None:
                ptrA = headB
            
            else: 
                ptrA = ptrA.next
            
            if ptrB is None:
                ptrB = headA
            
            else:    ptrB=ptrB.next
                
        return ptrA