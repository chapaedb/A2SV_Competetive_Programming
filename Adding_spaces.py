class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        resArr = []
        i = 0
        

        for index in spaces:
            portion = s[i:index]
            resArr.append(portion)
            i = index
            
   
        resArr.append(s[spaces[len(spaces) - 1]:])
        return " ".join(resArr)
