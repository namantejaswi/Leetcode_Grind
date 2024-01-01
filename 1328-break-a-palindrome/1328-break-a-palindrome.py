class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        
        palindrome = list(palindrome)
        if len(palindrome)==1:  return ""
        
        
        else:
            
            for i in range(len(palindrome)//2):
                
                
                # we try to insert 'a' at the earliest spot
                if palindrome[i]!='a':  
                    palindrome[i]='a'
                    return "".join(palindrome)
                    
        #if we have a string of all a's we insert b at the last position
        
        
        
        palindrome[-1]="b"
        
        
        return "".join(palindrome)