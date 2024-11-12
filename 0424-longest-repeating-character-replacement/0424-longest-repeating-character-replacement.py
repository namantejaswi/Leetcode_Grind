class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        
        #we keep count of the most frequent element in our window because when we shrink it could be that now another element is the most frequent 
        
        
        freq = {}
        l = 0
        mx_count = 0
        mx_l = 0
        
        
        for r in range(len(s)):
            
            if s[r] in freq:  freq[s[r]]+=1
                
            else:   freq[s[r]]=1
                
                
            mx_count = max(mx_count, freq[s[r]])
            
            #mx_count most frequent element in our current window
            
            
            #if current window exceeds mx_count+k remove l 
            
#          We never decrease max_count
# Even if the actual maximum frequency in the current window decreases, we keep the old max_count 
#This means our max_count might be "incorrect" (too high) for some windows

# Why this is okay:

# If we find a better answer later, we'll capture it because we're still updating max_count when adding new characters
# If we don't find a better answer later, then keeping the old max_count didn't affect our final result


            while r-l+1>mx_count+k:
                
                freq[s[l]]-=1
                l+=1
                
                
            mx_l = max(mx_l,r-l+1)
            
            
        return mx_l
                
            
            
            