class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else: 
            num = str(x)
            reversed_num = num[::-1]
            return num == reversed_num
