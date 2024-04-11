class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        start = 0
        char_index = {}

        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1
            length = end - start + 1
            max_length = max(max_length, length)
            char_index[s[end]] = end

        return max_length
            
