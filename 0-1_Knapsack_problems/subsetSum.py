from functools import lru_cache


class Solution():
    def td_SubsetSum(self, nums, target):
        n = len(nums)
        if n == 0:  return False

        @lru_cache
        def f(i, t):
            if t == 0:  return True
            if i < 0:   return False
            if t >= nums[i]:    return f(i-1, t) or f(i-1, t-nums[i])
            else:   return f(i-1, t)

        return f(n-1, target)
    


    def bu_SubsetSum(self, nums, target):
        n = len(nums)
        if target == 0: return True
        if n == 0:      return False

        dp = [[False]*(target+1) for i in range(n+1)]
        for i in range(n+1):    dp[i][0] = True
        for i in range(1, n+1):
            for j in range(1, target+1):
                if j >= nums[i-1]:  dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:   dp[i][j] = dp[i-1][j]


        return dp[n][target]




print(Solution().td_SubsetSum([2,3,7,8,10], 11))
print(Solution().bu_SubsetSum([2,3,7,8,10], 11))