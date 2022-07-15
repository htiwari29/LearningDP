from functools import lru_cache


class Solution():
    def td_EqualSumPartition(self, nums):
        n = len(nums)
        if n < 2:   return False
        total = sum(nums)
        if total%2 == 1:    return False

        @lru_cache
        def f(i, t):
            if t == 0:  return True
            if i < 0:   return False
            if nums[i] <= t:    return f(i-1, t) or f(i-1, t-nums[i])
            else:   return f(i-1, t)
        
        return f(n-1, total//2)


    
    def bu_EqualSumPartition(self, nums):
        n = len(nums)
        if n < 2:   return False
        target = sum(nums)
        if target % 2 == 1: return False
        dp = [[False]*(target//2 + 1) for i in range(n+1)]
        for i in range(n+1):    dp[i][0] = True
        
        for i in range(1, n+1):
            for j in range(1, target//2+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][target//2]





print(Solution().td_EqualSumPartition([1,5,11,5]))
print(Solution().bu_EqualSumPartition([1,5,11,5]))