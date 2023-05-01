class Solution:
    def get_combinations(amount: int, coins: List[int], coin_index: int, memory) -> int:
        if (amount, coin_index) in memory:
            return memory[(amount, coin_index)]
        if amount == 0:
            return 1
        if amount < 0 or coin_index == len(coins):
            return 0
        coin = coins[coin_index]
        combinations = Solution.get_combinations(amount - coin, coins, coin_index, memory)
        combinations += Solution.get_combinations(amount, coins, coin_index + 1, memory)
        memory[(amount, coin_index)] = combinations
        return combinations

    def iterative_solution(amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin,amount+1):
                dp[j] += dp[j-coin]
        return dp[-1]

    def change(self, amount: int, coins: List[int]) -> int:
        #MEMORY = {}
        #return Solution.get_combinations(amount, coins, 0, MEMORY)
        return Solution.iterative_solution(amount, coins)
