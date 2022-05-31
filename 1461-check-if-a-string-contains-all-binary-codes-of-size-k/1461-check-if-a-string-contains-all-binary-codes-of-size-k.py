class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        
        #Brute force check if all permutation are possible by generating all possible substring or better yet check the count of unique sub string if it is 2^k
        
        
        
        
        permutation=set()
        
        for i in range(len(s)-k+1):
        
            permutation.add(s[i:i+k])
            
        #print(permutation)
        return len(permutation)==2<<(k-1)
        
        	
        
        
        
        
        
        