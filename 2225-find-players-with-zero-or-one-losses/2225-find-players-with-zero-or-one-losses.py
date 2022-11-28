class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        
        lost_none=[]
        lost_one=[]
        
        lost_count={}
        
        for m in matches:
            
            w=m[0]
            l=m[1]
            
            if l not in lost_count:
                lost_count[l]=1
                
            elif l in lost_count:   lost_count[l]+=1
                
                
            if w not in lost_count: lost_count[w]=0
                
        for k,v in lost_count.items():
            
            if v==1:    lost_one.append(k)
                
            elif v==0:  lost_none.append(k)
                
        return [sorted(lost_none),sorted(lost_one)]
                