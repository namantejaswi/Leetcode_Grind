class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        
        
        special.sort()
        
        
        mx=0
        mx=max(top-special[-1],bottom-special[0],special[0]-bottom)
        print(mx)
        
        for i in range(0,len(special)-1):
            
            if special[i+1]==1+special[i]:
                       mx=max(mx,0)
                       
            else:  
                
                mx=max(special[i+1]-special[i]-1,mx)            
            
        return mx
            
            