# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        #Reverse the link list 
        #Remove the nth node
        #Reverse the link list again 
        
        #or traverse to get size then traverse again up until size-n
        
        #Both O(n) with T(n)=2*n+O(1) require 2 pass
        
        #for single pass, use 2 pointer time complexity remains same
        
        
        dummy_head=ListNode(0,head)      
        
        fastptr=dummy_head
        slowptr=dummy_head
        
        for i in range(0,n+1):
            fastptr=fastptr.next
            
        #we take fast to the nth elment from the begining
        
        while(fastptr!=None):
            fastptr=fastptr.next
            slowptr=slowptr.next
            
        slowptr.next=slowptr.next.next  #when fast ptr reaches the last node
                                        #slow ptr is 1 before the nth node from end
                                        #so we remove the elment by making next to next.next 
        return dummy_head.next