class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:    return
        
        min_word = min(strs,key=len)
        min_len=len(min_word)
        
        for index, string in enumerate(strs):
            
            if string[:min_len]==min_word:
                continue
                
            else:
                
                for i in range(len(string)):
                    if string[i]!=min_word[i]:
                        min_word = string[:i]
                        min_len=len(min_word)
                        break
                        
                        
                        
        return min_word
                    