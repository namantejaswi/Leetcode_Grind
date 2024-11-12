class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        
        #A tripplet can form a triangle if sum of 2 sides is greater than the third side
        
        #so we sort and then use 2 pointer from the element and count how many elments pair sum to greater than that
        
        
        
        nums.sort()
        cnt=0
        
        for n in range(len(nums)-1,-1,-1):
            
            largest_side = nums[n]
            
            l = 0 
            r = n-1
            
            
            while l<r:
                
                if nums[l]+nums[r] > largest_side:
                    
                    cnt+= r-l 
                    # 2,4,5,7,8,11.   4+8>11 so all elements between 4 and 8 can form a valid pair because we can keep 8 same and use all elements greater than 4 so 4,8 11  5,8,11 ,7,8,11 so number of elments between r-l pairs
                    
                    #decrement r now to find more such pairs
                    
                    r-=1
                    
                    
                #we cant find pairs with l l is too small increase it
                else:   l+=1
                    
                    
        return cnt
                    
            
            
            
            
        