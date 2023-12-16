class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        #Brute Force O(n^2)
#         prefix_sum = [0]*len(nums)
        
#         #the array prefix sum stores the sum of array upto the current index
        
        
#         curr=0
#         for i in range(len(nums)):
#             curr+=nums[i]
#             prefix_sum[i] = curr
            
            
#         #print(prefix_sum)
        
#         cnt=0
#         for i in range(len(prefix_sum)):
#             if prefix_sum[i]%k==0: cnt+=1
#             for j in range(i+1,len(prefix_sum)):
                
#                 if (prefix_sum[j]-prefix_sum[i])%k==0: cnt+=1
                
#         return cnt
        
    
       # ssave remainders of prefix sum
       #for -ve numbers addd +k  ancd check
        
        prefix_sum = [0]*len(nums)
        curr=0
        for i in range(len(nums)):
            curr+=nums[i]
            prefix_sum[i] = curr

        freq_rem = dict()
        freq_rem[0]=1
        
        res=0
        for i in prefix_sum:
            
            rem = (i%k)
            
            if rem<0:   rem = rem+k
                
            if rem not in freq_rem: freq_rem[rem]=1
                    
            elif rem in freq_rem:
                res+=freq_rem[rem]
                freq_rem[rem]+=1
                    
                    
        return res
                    
        
        
        
