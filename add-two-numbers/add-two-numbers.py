# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_head=ListNode(0);
        l3=dummy_head;
        
        s=0
        carry=0
        digit=0
        v1=0
        v2=0
        
        while(l1!=None or l2!=None or carry!=0):
            
            
            if(l1!=None): v1=l1.val
            else:
                v1=0            #add dummy zero, when we have l1<l2 
            
            if(l2!=None): v2=l2.val
            else:
                v2=0
                
            s=v1+v2+carry
            carry=s//10
            digit=s%10
            
            #For each digit we create a seperate node
            newNode=ListNode(digit)
            l3.next=newNode
            
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
            
            l3=l3.next 
            
            #Edge case of 2 single digits say 7+9 we check carry!=0
            
            
            
        return dummy_head.next