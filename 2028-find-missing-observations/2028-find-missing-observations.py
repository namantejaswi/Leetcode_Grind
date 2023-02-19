class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        
        total_sum = (len(rolls) + n)*mean
        
        #print(total_sum)
        
        target_sum = total_sum - sum(rolls)
        
        #we have n rolls to make up target_sum
        
        
        #we cant have n rolls to get sum greater than n*6 or less than n
        if target_sum > n*6 or target_sum < n: return []
        
        #if the above condition holds false then we definetly have a solution
        #we start by taking 1 and keep iterating until the target is zero 
        #to do the least steps we try to addd the largest numbers i.e 6
        
        target_sum-=n*1
        result = [1]*n
        
        while target_sum!=0:
            
            for i in range(len(result)):
                if target_sum<=5:
                    result[i]+= target_sum
                    target_sum-=target_sum  #moot point but sill
                    return result
                
                if target_sum>5:
                    
                    result[i]+=5
                    target_sum-=5
                    
        return result
            
        
        
        
        
    
        
        
        