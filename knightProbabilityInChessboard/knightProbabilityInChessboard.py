class Solution:
    # time complexity (n^2 * k * 8)
    # space complexity (n^2 * k)
    #This top down approach utilizes depth first search for the solution.

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        def dp(cur_k, cur_r, cur_c):
            if (cur_k, cur_r, cur_c) in memo:
                return memo[(cur_k, cur_r, cur_c)]

            if cur_k == K: #base case
                return 1

            ans = 0

            for d in moves:
                new_r = cur_r + d[0]
                new_c = cur_c + d[1]

                if 0 <= new_r < N and 0 <= new_c < N:
                    ans += 0.125 * dp(cur_k+1, new_r, new_c)

            memo[(cur_k, cur_r, cur_c)] = ans

            return ans

        memo = {}

        moves = ((-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2))

        return dp(0, r, c)
