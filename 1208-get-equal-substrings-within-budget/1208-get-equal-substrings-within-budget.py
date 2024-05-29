class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        
        left = 0 
        right = 0
        cost = 0
        mx = 0
        
        
        for right in range(len(s)):
            
            cost += abs(ord(s[right])-ord(t[right]))
            
            
            #remove element as long as max cost is exceeded by  shiftig left pointer
            while cost > maxCost:
                
                
                cost -=abs(ord(s[left])-ord(t[left]))
                left+=1
                
            
            curr = right - left + 1 
            mx = max(mx,curr)
            
            
            
        return mx
                
                
                
                
                
                
            
            
            