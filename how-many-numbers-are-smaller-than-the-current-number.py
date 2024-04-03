class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        
        counts = []
        for num in nums:
            count = sorted_nums.index(num)  
            counts.append(count)  
        
        return counts
