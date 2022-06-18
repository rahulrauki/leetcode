class Solution: # O(log n) time complexity beats 87,77 Number 2
    def search(self, nums: List[int], target: int) -> int:
        samp = nums
        while len(samp) > 0:
            mid = samp[len(samp)//2]
            if target == mid: return nums.index(mid)
            elif target < mid: samp = samp[0:len(samp)//2]
            else: samp = samp[1+len(samp)//2:]
        return -1

class Solution1: # One liner beats 99.24 97.28 Number 1
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1

class Solution2: #Number 3
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r ) // 2
            if nums[mid] < target : l = mid + 1
            elif nums[mid] > target : r = mid - 1
            else: return mid
        return -1