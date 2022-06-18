class Solution: # O(log n) time complexity beats 87,77
    def search(self, nums: List[int], target: int) -> int:
        samp = nums
        while len(samp) > 0:
            mid = samp[len(samp)//2]
            if target == mid: return nums.index(mid)
            elif target < mid: samp = samp[0:len(samp)//2]
            else: samp = samp[1+len(samp)//2:]
        return -1

class Solution1: # One liner beats 99.24 97.28
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1