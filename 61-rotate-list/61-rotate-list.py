# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        #calculating length of the linked list
        
        if not head: return
        if k==0 or not head.next:    return head
        
        itr=head
        l=0
        while(itr):
            l+=1
            if not itr.next:  break
            else:   itr=itr.next
        print(l)
        if k%l==0:    return head
    
        st=head
        c=1
            
        while(c!=l-(k%l)):
            
            c+=1
            st=st.next
        
        end=st.next
        
        itr.next=head
        st.next=None
        
        
        return end
        
   
        #Fails at l==k or l%k=0
        
        
        
        