# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
            root = head
            prev = root
            
            s = 0
            
            head = head.next
            while head:
                
                s+=head.val
                
                if head.val == 0:
                    
                    prev.val = s
                    
                    if head.next: 
                        prev.next = head
                    elif not head.next:
                        prev.next = None
                    prev = prev.next
                    s=0
                    
                    
                head=head.next
                
                
            return root
                    