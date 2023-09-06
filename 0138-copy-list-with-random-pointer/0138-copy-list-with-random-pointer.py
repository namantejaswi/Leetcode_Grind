"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        
        #The key idea is we have a dictionary of our nodes as while traversing throw
        
        
        if not head: return
    
    
        dic={}
        
        curr=head
        
        while(curr):
            
            
            dic[curr]=Node(curr.val)
            
            #cant set next and random as we dont have the next node and random yet
            
            curr=curr.next
               
        c=head
        
        while c:
            
            
            if c.next:  dic[c].next=dic[c.next]
            if c.random:    dic[c].random=dic[c.random]
            
            c=c.next
            
        return dic[head]
            