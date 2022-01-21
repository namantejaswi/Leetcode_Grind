class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
 
        min_val=min(nums)       
        max_val=sum(nums)   #Arbitrarilty high  for m=0
            
        
        #mid=(min_val+max_val)//2
        
        
        #Now we check if we can divide the array in m parts such that the max 
        #sum of any part is mid if not we increase our min_val to mid
        #if we can have the max value less than mid we update max_val to mid
        
        #i.e we use binary search to find the lowest possible value of the 
        #max of m subarrays, we take O(n) timeto check weather we can split           #the array into m  subbarray such that max of sub array subject to mid
        #we calculate mid in O(log n), so the overall time complexity is Ologn
        
        #To check if we can have m sub array with a max_val of mid we use a
        #counter for the number of subarray, in one linear pass the moment we
        #increase the sum greater than mid value we increment sub_array count 
        #if subarray count exceedes m then we 
        
        while(min_val<=max_val):
            

            mid=(min_val+max_val)//2
            print(mid)
            
            #now we check we can split the sub array 
            def checker(nums, mid, m):
                counter=1
                curr=0
                for i in range(len(nums)):
                    
                    curr+=nums[i]        
                    if curr>mid:
                        counter+=1
                        curr=nums[i]
                        if curr>mid:    return False
                        #if the single element is greater than mid the sub
                        #array will be greater given we have non negative int
                        
                    if counter >m:  return False
            
                return True
                    
            res=checker(nums,mid,m)
            print(res,mid)
            
    
            if res==True:
                max_val=mid-1
                
            elif res==False:
                min_val=mid+1
                
        return min_val
                
                
            
                    
                    
            
                        
                
        
        
        
        
        
        
        
        
        
        
        
        