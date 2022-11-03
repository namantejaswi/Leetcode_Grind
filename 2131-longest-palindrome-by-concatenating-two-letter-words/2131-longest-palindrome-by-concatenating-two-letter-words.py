class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        
        
        w=(Counter(words))
        print(w)
        
        
        pairs=0
        center=0
        res=0
        flag=0
        
        for word,count in w.items():
            
            if word[0]==word[1]:
                
                if count%2==0:
                    
                    res+=count
                    
                    
                else:   
                    res+=count-1 
                    flag=1
                    
            elif word[0]<word[1]:
                
                res+=2*min(count,w[word[1]+word[0]])
        if flag==1: res+=1
        return 2*res    
                
                
            