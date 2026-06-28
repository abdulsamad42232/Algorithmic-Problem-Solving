class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        diff = float('inf')
        nums.sort()
        l, r = 0, k-1
        while r<len(nums):
            diff = min(diff, nums[r]-nums[l])
            l, r = l+1 , r+1
        return(diff)       