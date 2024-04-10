class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = len(s) - 1
        vowels = ['a', 'e', 'i', 'o','u','A','E','I','O','U' ]
        res = list(s)
        while left < right:
            if res[left] in vowels:
                if res[right] in vowels:
                    res[left], res[right] = res[right], res[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            elif res[right] in vowels:
                if res[left] in vowels:
                    res[left], res[right] = res[right], res[left]
                    left += 1
                    right -= 1
                else:
                    left += 1
            else:
                left += 1
                right -= 1
        return ''.join(res)
