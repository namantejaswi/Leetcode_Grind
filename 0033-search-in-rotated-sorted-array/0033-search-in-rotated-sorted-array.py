class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        # in a rotated sorted array there are 2 monotonic increasing part and the end of one and start of another has a kink or max element
        
        # now we generally make our search space based on mid
        
        # here one of the 2 halves will be sorted
        
        l = 0
        r = len(nums)-1
        
        
        while(l<=r):       
            
            mid =(l+r)//2
            
            
            if nums[mid]== target:  return mid
            
            if nums[mid]>=nums[l]:

                #left half is sorted apply bs to [l,mid)

                
                #now what to do in left sorted half
                if target>=nums[l] and target<nums[mid]:

                    r = mid-1

                else:   l = mid+1

                    
            #right half is sorted apply binary search from (mid to r]

            elif nums[mid]<nums[l]:  #right half is sorted 


                if target >nums[mid] and target<=nums[r]:
                    l = mid+1

                else:   r=mid-1
                    
                    
                    
        return -1




            
            
            
            
            
        