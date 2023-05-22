# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        #calculate length of the linked list
        #now we need to swap k and l-k th node
        
        if not head.next:   return head
        h1=head
        
        l=0
        while(h1):
            
            l+=1
            h1=h1.next
            
        h2=head
        
        first=None
        second=None
        
        cnt=1
        while(h2):
            if cnt==k:   
                first= h2
            elif cnt == l-(k-1):
                second = h2
            cnt+=1
            h2=h2.next
            
        
        if first and second:first.val,second.val=second.val,first.val
        return head