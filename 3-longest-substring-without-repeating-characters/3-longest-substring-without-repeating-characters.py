class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_map=set()
        
        left=0
        right=0
        max_l=0
        
        
        for right in range(len(s)):
            
            while s[right] in char_map:
                
                char_map.remove(s[left])
                left+=1
                
            char_map.add(s[right])
            max_l=max(max_l,right-left+1)
            
        return max_l
            
        
            
            
            
                    