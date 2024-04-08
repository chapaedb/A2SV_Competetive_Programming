class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        
        total_coins = 0
        num_triplets = len(piles) // 3
        
        for i in range(1, 2*num_triplets, 2):
            total_coins += piles[i]
        
        return total_coins
