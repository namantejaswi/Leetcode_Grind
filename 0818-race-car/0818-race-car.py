class Solution:
    def racecar(self, target: int) -> int:
        
        
        q = deque([(0,1,0)])      #position, speed, length
        
        visited = set([(0,1)])    #position, speed
        
        while q:
            
            
            position, speed, moves = q.popleft()
            
            if position == target:
                
                return moves
            
            
            q.append((position + speed, speed*2, moves+1))
            
            #we will change the direction only when if we are in opposite direction moving towards -ve i.e left 
            
            if (speed<0 and position+speed <target) or (position+speed>target and speed>0): q.append((position,-speed/abs(speed),moves+1))
