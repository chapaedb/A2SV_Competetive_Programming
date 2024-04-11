class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_ = sum(nums[:k])
        max_ = sum_/k
        l = 0
        r = k
        while r < len(nums):
            sum_ -= nums[l]
            sum_ += nums[r]
            l += 1
            r += 1
            max_ = max(max_, sum_/k)
        return max_
