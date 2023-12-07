class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        x=0
        y=0
        def move(m):
            
            nonlocal x,y
            
            if m=="U": x+=1
            elif m =="D": x-=1
            elif m=="L":    y-=1
            elif m=="R":    y+=1
            
    
        for m in moves:
            
            move(m)
            
        return x==0 and y==0