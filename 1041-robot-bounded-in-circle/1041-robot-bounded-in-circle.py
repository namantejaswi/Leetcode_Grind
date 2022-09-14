class Solution:
    def isRobotBounded(self, s: str) -> bool:
        
        
        position=[0,0,0]   # 0-north,1-east,2-south,3-west
        #visited=set()
        
        #visited.add((0,0))
                
        for i in range(len(s)):
                
                #print(position)
                if s[i]=="G":
                    
                    if position[2]==3:
                        position[0]-=1
                        
                    if position[2]==1:
                        position[0]+=1
                        
                    if position[2]==0:
                        position[1]+=1
                    
                    if position[2]==2:
                        position[1]-=1
                    
                    #visited.add((position[0],position[1]))
                    
                     
                if s[i]=="L":
                    
                    position[2]=(position[2]-1)%4
                    
                if s[i]=="R":
                    position[2]=(position[2]+1)%4
         
        #print(position)
        return ((position[0]==0 and position[1]==0) or position[2]!=0)
        
                
                    
                    
            
            