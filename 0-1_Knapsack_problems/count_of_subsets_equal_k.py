from functools import lru_cache


class Solution():
    def td_CountOfSubset(self, nums, k):
        n = len(nums)
        if n == 0:  return 0
        
        @lru_cache
        def f(i, t):
            if t == 0:  return 1
            if i < 0:   return 0
            if t >= nums[i]:    return f(i-1, t) + f(i-1, t-nums[i])
            else:   return f(i-1, t)

        return f(n-1, k)
    


    def bu_CountOfSubset(self, nums, k):
        n = len(nums)
        if n == 0:  return 0
        dp = [[0]*(k+1) for i in range(n+1)]
        for i in range(n+1):    dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, k+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                
                else:
                    dp[i][j] = dp[i-1][j]


        return dp[n][k]


print(Solution().td_CountOfSubset([2,3,5,6,8,10], 10))
print(Solution().bu_CountOfSubset([2,3,5,6,8,10], 10))