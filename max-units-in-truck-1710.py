# Using reverse sort on unit number and greedy algorithm
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total = 0
        for box in sorted(boxTypes, key= lambda x: -x[1]):
            if not truckSize > 0: break
            if box[0] <= truckSize:
                total += box[0]*box[1]
                truckSize-=box[0]
            else:
                total +=truckSize*box[1]
                truckSize = 0    
        return total 