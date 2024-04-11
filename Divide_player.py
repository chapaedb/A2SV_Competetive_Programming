class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        n = len(skill)
        team = n/2
        if sum(skill) %  team == 0:
            target = sum(skill)/team
        else:
            return - 1
        skill.sort()
       
        right = n - 1
        left = 0
        sum_ = 0
        while left <= right:
           
            if skill[left] + skill[right] == target:
                
                sum_ += skill[left] * skill[right]
                right -= 1
                left += 1
            
            else:
                return - 1
       

        return sum_
