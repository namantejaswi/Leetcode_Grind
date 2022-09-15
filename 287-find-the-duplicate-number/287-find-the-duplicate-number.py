class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        slowptr=0
        fastptr=0
        
        #we think of each number in the array as the link to another index since we have all the number from 1 to n we can think of it as a linklist with index o as the starting node and the value at each node pointing to the next index and as we have a linklist with 2 numbers pointing to same index that is we will have a loop for the duplicate element
        
        while True:
            
            slowptr=nums[slowptr]
            fastptr=nums[nums[fastptr]]
            
            
            if slowptr==fastptr:    break
                
                                                                                               #                                                           __ __    
        #we have detected the cycle now we want to find where -----|     |
        #                                                          |__ __|
        #the  cyclic parts begins or the node which has 2 indegree                             #if the values are unique like in this case one could build an adjacency list           #find the node with indegree 2 as since there is only one duplicate 
        
        #to do it with constant extra space
        # let l be the linear part and let c be the circular part of linkedlist
        #let the slow and fast pointers meet at some point x in the circular part
        #this x could be the start but it is not necesssary that they meet at start 
        # now we have 3 parts l, x and c-x 
        
        #now we initialize another pointer at x and a start pointer at head of linear part now we increase both by 1 and then they will meet at the start of the loop, 
        
        #the proof is Fast = 2*slow
        #   l/2+x/2+(c-x)/2+x/2=l+x
        #=> l=c-x
        
        start=0
        ins=None
        
        while(True):
            
            if nums[start]==nums[slowptr]: 
                return nums[start]    
            
            else:   
                start=nums[start]
                slowptr=nums[slowptr]
                
                
                
                
                
        