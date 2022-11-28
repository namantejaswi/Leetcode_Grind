class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        
    
    
        #Sort by starting time 
        
        
        jobs=sorted((zip(startTime,endTime,profit)), key=lambda x:x[0])
    
        dp={}
        
        def schedule(n):
            
            if n in dp:    return dp[n]
            
            #if the next job deos not exist
            if n>=len(startTime):   return 0
            
            curr_profit=jobs[n][2]
            
            for i in range(n+1,len(startTime)):
                
                #we see how far can we go by doing the current job and taking all possible next non overlapping
                
                #if over lapp occurs it is taken care by the dp[n]=max(schedule(n+1),curr_profit) where in the schedule(n+1) wont take nth job
                
                
                # if the nth job ends before the start of ith job we can do
                
                if jobs[n][1]<=jobs[i][0]:
                    curr_profit+=schedule(i)
                    break
            
            #we select the max of doing n+1 or the curr
            dp[n]=max(schedule(n+1),curr_profit)
            
            return dp[n]
        
        schedule(0)
        
        #the dp dictionary stores the best profit starting from job 1,2,3 until end
        #print(dp)
        
        return dp[0]    
    
    
    
    
    
    
    
    
    
    
    