class Solution:
    def numTrees(self, n: int) -> int:
        
        #Catalan Number if you know you know
        
        
        catalan= [0 for i in range(n+1)]
        catalan[0]=1
        catalan[1]=1
        
        for i in range(2,n+1):
            for j in range(1,i+1):
                
                catalan[i]+=catalan[j-1]*catalan[i-j]
                
                
                
        return catalan[n]