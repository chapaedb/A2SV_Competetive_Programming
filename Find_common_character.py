class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        min_word = min(words, key=len)
        common_chars = []

        for char in min_word:
            if all(char in word for word in words):
                common_chars.append(char)
                words = [word.replace(char, '', 1) for word in words]

        return common_chars
