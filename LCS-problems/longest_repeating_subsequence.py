
class Solution():
    def longestReapeatingSubsequence(self, s):
        n = len(s)
        if n == 0 or n == 1:
            return 0
        
        dp = [[0]*(n+1) for i in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == s[j-1] and i != j:
                    dp[i][j] = dp[i-1][j-1] + 1
                
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[n][n]


print(Solution().longestReapeatingSubsequence("AABBCEDD"))