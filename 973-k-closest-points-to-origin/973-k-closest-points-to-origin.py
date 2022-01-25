class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        
        dis={}
    
        index=0
        for cordinate in points:
            
            d=sqrt(((cordinate[0]-0)**2) + ((cordinate[1]-0)**2))
            
            dis[index]=d
            index+=1
            
        #print(dis)
        
        s_dis=(dict(sorted(dis.items(), key=lambda item: item[1])))
        
        #print(s_dis)
        
        res=[]
        for i in s_dis.keys():
            res.append(i)
        
        #print(res)
        
        ans=[]
        
        for i in range(k):
            
            ans.append(points[res[i]])
        
        
        return ans
        
        
        
        