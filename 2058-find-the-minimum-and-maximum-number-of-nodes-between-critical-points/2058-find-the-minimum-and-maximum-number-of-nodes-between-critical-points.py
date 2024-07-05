# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        
        min_dist = float("inf")
        
        first_critical = None
        last_critical = None 
        
        root = head
        prev = root
        
        head = head.next
        cnt=0
        
        while head:
            
            if head.next:
                
                
                cnt +=1
                if (prev.val < head.val and head.next.val <head.val) or (prev.val>head.val and head.val<head.next.val):
                    #print("cnt",cnt,head.val)
                    if first_critical is None:
                        
                        first_critical = cnt
                        
                    elif first_critical:
                        
                        if last_critical:

                            min_dist = min(min_dist,cnt-last_critical)
                            last_critical = cnt

                        elif not last_critical:  
                            last_critical = cnt
                            min_dist = min(min_dist,last_critical-first_critical)
                        
            head=head.next  
            prev=prev.next

                        
        #(first_critical,last_critical)  
        if not first_critical or not last_critical: return [-1,-1]
        return [min_dist,last_critical-first_critical]
                
            