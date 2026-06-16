class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not isinstance(prices, List) or not prices:
            return 0

        max_final = 0
        for i in range(len(prices)):
            max_current = 0
            for t in range(len(prices)):
                if t > i:
                    max_current = max(0, max_current, prices[t]-prices[i])
                else:
                    continue
            max_final = max(0, max_final, max_current)

        
        return max_final



        