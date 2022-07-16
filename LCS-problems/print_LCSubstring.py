
class Solution():
    def print_lc_substring(self, s, t):
        m = len(s)
        n = len(t)

        if m == 0 or n == 0:
            return ""
        
        ans = ""
        dp = [[""]*(m+1) for i in range(n+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + s[i-1]
                
                if len(ans) <= len(dp[i][j]):
                    ans = dp[i][j]
        
        return ans

print(Solution().print_lc_substring("abcde", "abfce"))

