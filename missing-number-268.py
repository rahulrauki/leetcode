class Solution1: # Using the summation of linear array formula - n*(n+1)/2 == sum(range(n+1)) 230ms, 15.2mb
    def missingNumber(self, nums) -> int:
        n = len(nums)
        return n * (n+1)//2 - sum(nums)

class Solution: #Using set because of unique numbers - 135ms,15.9mb
    def missingNumber(self, nums) -> int:
        set1 = set(nums)
        for i in range(len(nums)+1):
            if i not in set1:
                return i

