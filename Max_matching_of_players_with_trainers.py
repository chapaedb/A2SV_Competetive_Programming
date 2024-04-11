class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        matching = 0
        players.sort()
        trainers.sort()
        while left < len(players) and right < len(trainers):
            if players[left] <= trainers[right]:
                matching += 1
                left += 1
            right += 1
        return matching
