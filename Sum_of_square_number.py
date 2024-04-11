class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left = 0
        right = int(sqrt(c))
        
        while left <= right:
            current_sum = left * left + right * right
            
            if current_sum == c:  
                return True
            elif current_sum < c:  
                left += 1
            else:  
                right -= 1
        
        return False  
