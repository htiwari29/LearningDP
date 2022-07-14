from functools import lru_cache


class Solution():
    def tdZeroOneKnapsack(self, weights, values, w):
        n = len(weights)
        if n == 0:  return 0
        
        @lru_cache
        def f(t, i):
            if t == 0:  return 0
            if i < 0:   return float('-inf')
            if t >= weights[i]: return max(f(t, i-1), values[i]+f(t-weights[i], i-1))
            else:   return f(t, i-1)

        return f(w, n-1)
    


    def buZeroOneKnapsack(self, weights, values, w):
        n = len(weights)
        dp = [[-1]*(w+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(w+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0

        for i in range(1, n+1):
            for j in range(1, w+1):
                if j >= weights[i-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])

                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][w]


print(Solution().tdZeroOneKnapsack([1,3,4,5], [1,4,5,7], 7))
print(Solution().buZeroOneKnapsack([1,3,4,5], [1,4,5,7], 7))

        