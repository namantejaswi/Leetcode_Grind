class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        
        freq={}
        
        if len(s)==1:
            return True
        
        for i in s:
            
            if i not in freq:
                freq[i]=1
                
            else:
                freq[i]+=1
                
                
        #Now a palindrome is possible if number of chars are even then 
        #the frequency of each element should be even
        #if number of chars is odd except one element all chars count to be even
        #if single char it is already palindrome
        
        
        if len(s)%2==0:
            
            flag=True
            for i in freq:
                if freq[i]%2!=0:
                    flag=False
                    return flag
                
            return flag
        
        count=0
        
        if len(s)%2==1:
            flag=True
            for i in freq:
                if freq[i]%2!=0:
                    if count ==0:
                        count=1
                        
                    else:
                        flag=False
                        return flag
                    
            return flag
                
                
                
            
            
                
            
        