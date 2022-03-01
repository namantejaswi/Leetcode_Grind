class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        freq={}
        
        for i in arr:
            
            if i not in freq:
                freq[i]=1
                
            freq[i]+=1
            
        f=freq.values()
        return len(f)==len(set(f))