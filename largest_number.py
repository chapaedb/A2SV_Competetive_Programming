class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def check(j):
            if str(nums[j]) + str(nums[j + 1]) < str(nums[j + 1]) + str(nums[j]):
                return True
            return False
        for i in range(len(nums)):
            for j in range(len(nums) - (i + 1)):
                if check(j):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        ans = "".join(map(str, nums))
        if int(ans) == 0:
            return "0"
        return ans
