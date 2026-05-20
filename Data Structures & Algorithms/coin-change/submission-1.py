class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if amount in memo:
                return memo[amount]

            best = float('inf')
            for coin in coins:
                best = min(best, 1 + dfs(amount-coin))
            
            memo[amount] = best

            return best
        
        answer = dfs(amount)
        return -1 if answer == float("inf") else answer