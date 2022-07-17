class Solution:
    # time complexity (n^2 * k * 8)
    # space complexity (n^2 * k)
    #This top down approach utilizes depth first search for the solution.

    # def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
    #     def dp(cur_k, cur_r, cur_c):
    #         if (cur_k, cur_r, cur_c) in memo:
    #             return memo[(cur_k, cur_r, cur_c)]
    #
    #         if cur_k == K: #base case
    #             return 1
    #
    #         ans = 0
    #
    #         for d in moves:
    #             new_r = cur_r + d[0]
    #             new_c = cur_c + d[1]
    #
    #             if 0 <= new_r < N and 0 <= new_c < N:
    #                 ans += 0.125 * dp(cur_k+1, new_r, new_c)
    #
    #         memo[(cur_k, cur_r, cur_c)] = ans
    #
    #         return ans
    #
    #     memo = {}
    #
    #     moves = ((-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2))
    #
    #     return dp(0, r, c)

        moves = ((-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2))

        dp = [[[0] * N for _ in range(N)] for _ in range(K+1)]

        dp[0][r][c] = 1 #base case

        for k in range(1, K+1):
            for i in range(N):
                for j in range(N):
                    for d in moves:
                        old_i = i + d[0]
                        old_j = j + d[1]

                        if 0 <= old_i < N and 0 <= old_j < N:
                            dp[k][i][j] += 0.125 * dp[k-1][old_i][old_j]
        ans = 0

        for i in range(N):
            for j in range(N):
                ans += dp[K][i][j]

        return ans
        # time complexity is the same as the top down approach
