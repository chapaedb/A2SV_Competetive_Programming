class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        nums.sort()
        for index, i in enumerate(nums):
            if i == target:

                ans.append(index)
        return ans
