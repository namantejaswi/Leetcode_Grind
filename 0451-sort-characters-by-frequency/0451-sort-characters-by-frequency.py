class Solution:
    def frequencySort(self, s: str) -> str:
        
        
        dic=dict(Counter(s))
        dic = dict(sorted(dic.items(),key=lambda x:-x[1]))
        
        res=""
        for key,val in dic.items():
            
            res+=key*val
            
        return res