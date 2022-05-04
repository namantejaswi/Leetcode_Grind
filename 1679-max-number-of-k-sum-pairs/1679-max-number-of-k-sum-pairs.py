class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        
        #Find number of disjoint pairs which sum up to k
        
        freq={}
        
        for i in nums:
            if i not in freq:
                
                freq[i]=1
                
            else:   freq[i]+=1
                
                
        pairs=0
                
        for i in freq:
            
            
            
            if i*2==k:
                
                pairs+=freq[i]//2
                
                #print("pair",i,i ,"ussed as",freq[i]//2,"pairs " "freq updated",freq[i]%2)
            
                freq[i]=freq[i]%2
            
            
            elif k-i in freq:
                
                
                #print("pair",i , k-i,"current freq",freq[i],freq[k-i])
                pairs+=min(freq[i],freq[k-i])
                
                mi=min(freq[i],freq[k-i])
                
                freq[k-i]-=mi
                freq[i]-=mi
                
                #print("updated freq",freq[k-i],freq[i])
        return pairs