class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        left = 0
        right = 0
        merg = []
        w1 = list(word1)
        w2 = list(word2)
        
        while left < len(w1) and right < len(w2):
            if w1[left] > w2[right]:
                merg.append(w1[left])
                left += 1
            elif w2[right] > w1[left]:
                merg.append(w2[right])
                right += 1
            else:
                
                if w1[left:] > w2[right:]:
                    merg.append(w1[left])
                    left += 1
                else:
                    merg.append(w2[right])
                    right += 1
        
        merg.extend(w1[left:])  
        merg.extend(w2[right:]) 
        
        return ''.join(merg)  
