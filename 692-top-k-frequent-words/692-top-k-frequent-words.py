class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        dic={}
        
        
        for i in words:
            
            if i not in dic:
                dic[i]=1
                
            else:   dic[i]+=1
                
        
          
        sorted_dic=sorted(dic,key=lambda x:(-dic[x],x))

        return sorted_dic[:k]
        
        
        