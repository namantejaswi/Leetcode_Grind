# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        
        
        #find mid reverse 2nd half and find max ez
        
        
        slow,fast=head,head
        
        while fast and fast.next:   #even input given
            
            fast=fast.next.next
            slow=slow.next
            
        #print(slow.val)
        
        #reverse 2nd half
        
        curr=slow
        prev=None
        
        
        
        
        while  curr!=None:
            
            forward=curr.next
            curr.next=prev
            prev=curr
            curr=forward
            
            
            

            
        mx=float('-inf')   
        while prev:
            
            mx=max(mx,head.val+prev.val)
            head=head.next
            prev=prev.next
            
            
        return mx