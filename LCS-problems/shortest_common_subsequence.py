
class Solution():
    def shortest_common_subsequence(self, s, t):
        m = len(s)
        n = len(t)

        if m == 0 or n == 0:
            return m if m else n
        
        dp = [[0]*(n+1) for i in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return m + n - dp[m][n]


print(Solution().shortest_common_subsequence("AGGTAB", "GXTXAYB"))
