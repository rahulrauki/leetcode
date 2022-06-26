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

#The Solution by subtracting the index from the inital window sum - method
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftSum,rightSum = sum(cardPoints[:k]),0
        maxi = leftSum
        for i in range(k):
            leftSum -= cardPoints[k-i-1]# [k-(i+1)] or just [k-i] if i starts from 1
            rightSum += cardPoints[-i-1]
            add = leftSum + rightSum
            if add > maxi: maxi = add
        return maxi