class Solution: # O(log n) time complexity 
    def search(self, nums: List[int], target: int) -> int:
        samp = nums
        while len(samp) > 0:
            mid = samp[len(samp)//2]
            if target == mid: return nums.index(mid)
            elif target < mid: samp = samp[0:len(samp)//2]
            else: samp = samp[1+len(samp)//2:]
        return -1