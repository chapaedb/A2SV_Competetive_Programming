class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                if nums[left] == 0:
                    nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return nums
