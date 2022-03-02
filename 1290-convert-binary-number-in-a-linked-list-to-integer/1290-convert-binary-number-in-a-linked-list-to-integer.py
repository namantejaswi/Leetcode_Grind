# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        
        res=0
        count=0
        
        k=0
        dum=head
        while dum:
            dum=dum.next
            k+=1
            
        print(k)
        
        k=k-1 #indexed power from 0
        while head:
            
            if k==0 and head.val==0:
                res+=0
                head=head.next
                k-=1
            else:    
                res+=(2*head.val)**k
                head=head.next
                k-=1
        return res