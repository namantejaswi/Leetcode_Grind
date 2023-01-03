# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        
        #for even next elem as mid
        
        slow=fast=head
        
        while fast and fast.next:
            
            slow=slow.next
            fast=fast.next.next
            
        mid=slow
            
            
        #we now need to reverse the second half of the linked list and then take one from first half and one from second 
        
        
        curr = mid
        prev = None
        forward = None
        
        
        while(curr):
            
            
            forward=curr.next
            curr.next=prev
            
            prev=curr
            curr=forward
        
        new_h2=prev     #curr is now null since we mark it to forward
        
                
        
        h1=head
        h2=new_h2
        
        
        while h2.next:
            
            first_neighbour=h1.next
            h1.next=h2
            h1=first_neighbour
            
            
            second_neighbour = h2.next
            h2.next = h1
            h2=second_neighbour
            
        