class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None :
            return ""
        smallest = min(strs, key = len)
        common = ""
        
        for i in range(len(smallest)):
            for j in range(len(strs)):
                 if strs[j][i] != smallest[i]:
                    return common

            common += smallest[i]        
        return common
