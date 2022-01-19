# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        
        new_node=ListNode()
        new_node.next=head
        
        prev=new_node
        curr=head
        
        while(curr):
            
            if curr.val==val:
                prev.next=curr.next
                curr=curr.next
                
            else:
               
                prev=curr
                curr=curr.next
                
                
        return new_node.next