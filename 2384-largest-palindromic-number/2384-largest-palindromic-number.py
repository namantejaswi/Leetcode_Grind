class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        freq= {}
        
        for i in range(len(num)):
                       
            
            if (num[i]) not in freq:
                       freq[num[i]] =  1
                       
            else:   freq[num[i]] += 1
          
        
                   
        freq_sorted =dict( sorted(freq.items(), key = lambda x:x[0]))
        #print(freq_sorted)
        
        largest_odd = None
        
        #print(not(largest_odd))
        for k,v in freq_sorted.items():
            
            if v%2==1:  largest_odd= k #[number,cnt]
                
        #print(largest_odd)
        
        #we use largest-odd over zero as center
        #we can fill zero in the center as long as we got 2 digits
        
        if len(freq)==1 and '0' in freq:    return "0"
        res=""
        for k,v in freq_sorted.items():
                
                if k!='0':
                    res+=int(v//2) *k
            
    
        if not largest_odd: 
            
            first_half = res[::-1]
            if '0' not in freq or len(first_half)<1: 
                res = res[::-1] + res
                return res
        if largest_odd: 
            first_half = res[::-1]
            
            if '0' not in freq or len(first_half)<1:
                res = res[::-1] + largest_odd+res
                return res
        
        #if we have zeros we can use all zeros with no odd freq as long as their is a first half
        #with even freq we can use all zeros
        
        
        if not largest_odd: res= res[::-1]+ freq['0']*'0'+res
        
        if largest_odd: res = res[::-1] + int(freq['0']//2)*'0' + largest_odd + int(freq['0']//2)*'0' + res
        return res
            
        
        
        
        