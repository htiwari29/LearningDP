
class Solution():
    def print_lcs(self, s, t):
        m = len(s)
        n = len(t)
        if m == 0 or n == 0:
            return 0
        
        dp = [[""]*(n+1) for i in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1] and len(dp[i][j]) <= len(dp[i-1][j-1])+1:
                    dp[i][j] = dp[i-1][j-1] + s[i-1]

                else:
                    if len(dp[i-1][j]) >= len(dp[i][j-1]):
                        dp[i][j] = dp[i-1][j]
                    
                    else:
                        dp[i][j] = dp[i][j-1]
        

        return dp[m][n]


    # Approach 2, Better. Use LCS Dp table to generate string


print(Solution().print_lcs("abcdgh", "abedfhr"))


