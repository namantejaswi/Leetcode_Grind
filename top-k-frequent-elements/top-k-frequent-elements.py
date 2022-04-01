class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq={}
        
        for i in nums:
            if (i not in freq):
                freq.update({i:1})
            else:
                freq[i]=freq[i]+1
             
        arr = sorted(freq, key = freq.get,reverse = True)
        #sort by the values in freq in reverse order 
        
        #print(freq)
        
        #print(arr)          #Keys sorted by value of corresponding key 
        
        #b=sorted(freq)      #keys Sorted by quantity of key
        #print(b)
        
        return(arr[:k])