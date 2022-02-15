class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        
        boxTypes=sorted(boxTypes,reverse=True,key=lambda x:x[1])
        print(boxTypes)
        
        #greedy
        
        units=0
        count=0
        
        for i in range(len(boxTypes)):
            if count>=truckSize:
                break
            
            
            if count+boxTypes[i][0]<=truckSize:
                units+=boxTypes[i][0]*boxTypes[i][1]
                count+=boxTypes[i][0]
            
            else:
                while (boxTypes[i][0]>0):
                    if count>=truckSize:    
                        return units 
                        
                    else:   
                        count+=1
                        boxTypes[i][0]-=1
                        units+=boxTypes[i][1]
                    
                    
        return units
            