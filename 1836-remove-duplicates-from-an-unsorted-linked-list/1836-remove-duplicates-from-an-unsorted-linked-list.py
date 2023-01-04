# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
       
    
    
    #find all duplicates in one pass
    #skip duplicates
    

        seen_once=set()
        seen_multiple=set()

        h=head

        while head:

            if head.val not in seen_once and head.val not in seen_multiple:

                seen_once.add(head.val)

            else:   
                seen_multiple.add(head.val)
                
                if head.val in seen_once:seen_once.remove(head.val)
            head=head.next

        
        
        new_head =ListNode(0,h)  #new node with next as head
        sent=new_head    
            
        
        while new_head.next:
            
            
            if new_head.next.val not in seen_once:
                
                new_head.next=new_head.next.next
                
                
    
            else:   new_head=new_head.next
                
                

                
                
        return sent.next
                
                