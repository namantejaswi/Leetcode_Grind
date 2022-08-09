class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        
    
        
        arr.sort()
        
        dp=[1]*len(arr)
        
        arr_set=set(arr)
        
        num_idx={num:i for i,num in enumerate(arr)}        
                
        n=len(arr)
        
        for i in range(1,n):

            for j in range(i):
                
                if arr[i]%arr[j]==0:
                    
                    fact_complement=arr[i]//arr[j]
                    
                    #if we have the 2nd factor  also 
                    
                    
                    if fact_complement in arr_set:
                        
                        index_fc = num_idx[fact_complement]
                        
                        dp[i]+=dp[j]*dp[index_fc]
                        
                        #as we can use a number as many times
                        
                        
        return sum(dp)%((10**9)+7)
                        
                    
                    
        