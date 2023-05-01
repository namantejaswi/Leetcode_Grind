class Solution:
    def average(self, salary: List[int]) -> float:
        
        s,l=0,0
        mi=float('inf')
        mx=float('-inf')
        
        
        for i in salary:
            s+=i
            l+=1
            mx=max(i,mx)
            mi=min(i,mi)
            
        return (s-mi-mx)/(l-2)
    
    