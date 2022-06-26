"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', val: int) -> 'Node':
        orignal=head
        begin=head
        
        if head==None:    
            new_node=Node(val)
            new_node.next=new_node
            return new_node
        
        if head.next==head:
            if val>=head.val:
                n=Node(val)
                head.next=n
                n.next=head
                return n.next
            else:
                n=Node(val)
                n.next=head
                head.next=n
                return head
            
            
        #if head is the max or min of the new list then add it at the end
        
        found_a_greater=False
        found_a_smaller=False
        start=head
        mx_node=Node()
        mx_val=-10**7
        min_val=10**7
        min_node=Node()
        
        while(head.next!=start):
            if head.val>=val:
                found_a_greater=True
            if head.val<=val:
                found_a_smaller=True    
            if head.val>=mx_val:
                mx_val=head.val
                mx_node=head
            if head.val<=min_val:
                min_val=head.val
                min_node=head
            head=head.next
           
        if head.val>=val:   found_a_greater=True
        if head.val<=val:   found_a_smaller=True
        
        if head.val<=min_val:    min_node=head
        if head.val>=mx_val:    mx_node=head
            
        
        #if all the elments are same and the elment to be added is same    
        if not(found_a_greater) and not(found_a_smaller):
            
            n=Node(val)
            head.next=n
            n.next=start
            return n.next
            
        
        #if all the elments are smaller then we add after the largest element
        
        if not(found_a_greater) and found_a_smaller or (found_a_greater and not found_a_smaller):
            #enter after the largest node
            while(begin!=mx_node):
                begin=begin.next
                
                
            n=Node(val)
            to_connect=begin.next
            begin.next=n
            n.next=to_connect
            
            return orignal
        
            
        else:
            head=orignal
            #print(head.val)
            while(True):

                if head.val<=val and head.next.val>=val:
                    inserting_after=head
                    temp=head
                    n=Node()
                    n.val=val
                    n.next=temp.next
                    head.next=n

                    break

                else:   head=head.next


        return orignal