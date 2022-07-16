
class Solution():
    def lc_substring(self, s, t):
        m = len(s)
        n = len(t)
        if m == 0 or n == 0:
            return 0

        dp = [[0]*(n+1) for i in range(m+1)]

        ans = float("-inf")

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                
                else:
                    dp[i][j] = 0

                ans = max(ans, dp[i][j])
                
        return ans


print(Solution().lc_substring("abcde", "abfce"))