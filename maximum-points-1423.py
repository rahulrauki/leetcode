#Using Sliding window, correct but time limit exceeded
#Idea is to remove the index from lSum instead of referencing
# each time, that can reduce the slicing time
class Solution:# 
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftSum = sum(cardPoints[:k])
        maxi = leftSum
        for i in range(1,k+1):
            window = sum(cardPoints[:k-i]) + sum(cardPoints[-i:])
            if window > maxi: maxi = window
        return maxi