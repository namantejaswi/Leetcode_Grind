class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        
        dic={}
        
        for id_score in items:
            
            name=id_score[0]
            score=id_score[1]
            
            if name not in dic:
                
                dic[name]=[score]
                
            else:   dic[name].append(score)
                
                
        res=[]
        
        
        for s in dic:
            
            dic[s]=sorted(dic[s],reverse=True)
            
        for v in dic:
            
            
            dic[v]=sum(dic[v][:5])//5
            
            
        for key,val in dic.items():
            
            res.append([key,val])
            
        return sorted(res,key= lambda x:x[0])
                