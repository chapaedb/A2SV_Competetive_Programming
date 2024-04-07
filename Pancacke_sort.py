class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        
        for i in range(len(arr), 1, -1):
            max_index = arr.index(i)
            arr[:max_index + 1] = reversed(arr[:max_index + 1])
            arr[:i] = reversed(arr[:i])
            flips.extend([max_index + 1, i])

        return flips
