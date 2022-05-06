class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        
        
        #start at the station with the max [gas-cost to next station] 
        #which is the same as min of cost to next - gas you get
        
        
        net_fuel=[]
        
        for i in range(len(gas)):
            
            net_fuel.append(gas[i]-cost[i])
            
        #print(net_fuel)
        
        if sum(net_fuel)<0: return -1
        
        #Total fuel used up to this point, running sum
        
        s=[0]*len(gas)    #Running sum
      
        curr=0
        for i in range(len(gas)):
            
            s[i]+=curr+net_fuel[i]
            curr=s[i]    
        
        #print(s)
                
        #you start at the point after which the net sum is lowest         
        #mod in case it is the last index to make circular 
        return (s.index(min(s))+1)%len(gas)
                