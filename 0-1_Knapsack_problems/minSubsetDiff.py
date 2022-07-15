
class Solution():
    def td_MinSubsetDiff(self, nums):
        n = len(nums)
        if n < 2:   return -1
        target = sum(nums)

        dp =[[False]*(target//2+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        
        for i in range(1, n+1):
            for j in range(1, target//2+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                
                else:
                    dp[i][j] = dp[i-1][j]
        

        ans = float("inf")
        for j in range(target//2+1):
            if dp[n][j]:
                ans = min(ans, target- 2*j)
        
        return ans





print(Solution().td_MinSubsetDiff([1,6,11,5]))
print(Solution().td_MinSubsetDiff([1,2,7]))


        