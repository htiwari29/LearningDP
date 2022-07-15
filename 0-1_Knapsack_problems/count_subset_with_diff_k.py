
class Solution():
    def count_subset_with_diff_k(self, nums, k):
        n = len(nums)
        if n < 2:   return 0
        target = sum(nums)

        # s1+s2 = target
        # s1-s2 = k
        # from above:   s1 = (k+target)//2

        new_target = (k + target)//2
        dp = [[0]*(new_target+1) for i in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, new_target+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]] 
                
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][new_target]




print(Solution().count_subset_with_diff_k([1,1,2,3],1))


                