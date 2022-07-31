class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])

        dp = points[0]

        leftToRight = [0] * n
        rightToLeft = [0] * n

        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    leftToRight[j] = dp[j]
                else:
                    leftToRight[j] = max(leftToRight[j-1]-1, dp[j])

            for j in range(n-1, -1, -1):
                if j == n-1:
                    rightToLeft[j] = dp[j]
                else:
                    rightToLeft[j] = max(rightToLeft[j+1]-1, dp[j])

            for j in range(n):
                dp[j] = points[i][j] + max(leftToRight[j], rightToLeft[j])

        return max(dp)
