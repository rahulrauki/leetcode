#This is not optimal O(n), this uses timsort so its asymptotic O(nlogn)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        biggest,current,lis = 0,0,sorted(nums)
        if len(nums) == 0 : return 0
        for i in range(len(lis)-1):
            if lis[i+1] - lis[i] == 1: current+=1
            elif lis[i+1] == lis[i]: pass
            else:
                if current > biggest: biggest = current
                current = 0
        if biggest < current: biggest = current
        return biggest + 1