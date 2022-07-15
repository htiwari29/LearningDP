from functools import lru_cache


class Solution():
    def td_LCS(self, s, t):
        m = len(s)
        n = len(t)
        if m == 0 or n == 0:
            return 0
        
        @lru_cache
        def f(a, b):
            if a<0 or b<0:  return 0
            if s[a] == t[b]:    return 1 + f(a-1, b-1)
            else:   return max(f(a-1, b), f(a, b-1))
        
        return f(m-1, n-1)


    
    def bu_LCS(self, s, t):
        m = len(s)
        n = len(t)
        if m == 0 or n == 0:
            return 0
        
        dp = [[0]*(n+1) for i in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        

        return dp[m][n]



print(Solution().td_LCS("abcdgh", "abedfhr"))
print(Solution().bu_LCS("abcdgh", "abedfhr"))