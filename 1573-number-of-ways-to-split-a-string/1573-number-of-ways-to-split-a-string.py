class Solution:
    def numWays(self, s: str) -> int:
        
        
        #If the number of ones in the string is not divisible by 3 we simply
        #cannot divide the entire string into 3 parts having equal number of 1
        
        #if count is zero we can return any 3 parts
        #the number of ways to divide string into 3 parts is nc2=n-1*n/2 or
        #we have to select 2 places to slice in a sting of n char
        #n-2+ n-3 + n-4 + n-5 ... 1 = (n-2)*(n-1)/2
        
        count=0
        mod=(10**9)+7
        
        for i in s:
            if i=="1":
                count+=1
                
        l=len(s)        
        if count==0:    return ((l-1)*(l-2)//2) % mod
        
        if count%3!=0:  return 0
        
        
        ones_in_each_block = count/3
        
        no_first_partion=0
        no_second_partion=0
        
        
        cnt=0
        for ch in s:
            
            if ch=="1":
                cnt+=1
                
            if cnt == ones_in_each_block:
                
                no_first_partion+=1
                
            elif cnt == 2 * ones_in_each_block:
                
                no_second_partion+=1
                
                
        return (no_first_partion * no_second_partion) % mod
            
                
        
       
        
        