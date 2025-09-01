class Solution:
    def climbStairs(self, n: int) -> int:
        self.dp = [0]*(n+1)
        return self.solve(n)

    def solve(self,n):
        if n==1:
            return 1
        elif n==2:
            return 2
        if self.dp[n]!=0:
            return self.dp[n] 
        self.dp[n] = self.solve(n-1) + self.solve(n-2)
        return self.dp[n]