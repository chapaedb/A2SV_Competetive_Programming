class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        left = 0
        right = len(people) - 1

        people.sort()
        boat = 0
        while right >= left:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1    
                boat += 1
            elif people[left] + people[right] > limit:
                if people[right] <= limit:
                    boat += 1
                right -= 1
            
            else:
                left += 1
                
    
        return boat
        

