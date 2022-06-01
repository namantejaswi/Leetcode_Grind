class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        
        
        palindrome=list(palindrome)
    
        if len(palindrome)==1:  return ""
        
        if len(set(palindrome))==1: 
            pass
        
        for i in range(len(palindrome)):
            
            
            if len(palindrome)%2==0 or i!=((len(palindrome)//2)+1)-1:
        
            
                if palindrome[i]!='a':
                    palindrome[i]='a'
                    return (''.join(palindrome))
            
                
        palindrome[-1]='b'
        return (''.join(palindrome))
            