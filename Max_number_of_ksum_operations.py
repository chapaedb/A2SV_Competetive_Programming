class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n - 1
        op = 0
        nums.sort()
        while right > left:
            if nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                op += 1
                right -= 1
                left += 1
        return op
