class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def getSubArrCountWithTarget(arr):
            sum_dict = defaultdict(int)
            #base case
            sum_dict[0] = 1
            ans = 0
            running_sum = 0

            for num in arr:
                running_sum += num
                target_sum = running_sum - target

                if target_sum in sum_dict:
                    ans += sum_dict[target_sum]

                sum_dict[running_sum] += 1

            return ans

        pre_sum = []

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            cur_sum = []
            for j in range(n):
                if j == 0:
                    cur_sum.append(matrix[i][j])
                else:
                    cur_sum.append(matrix[i][j] + cur_sum[-1])

            pre_sum.append(cur_sum)

        ans = 0

        # fix two colums
        for c2 in range(n):
            for c1 in range(c2+1):
                cur_arr = []

                for i in range(m):
                    row_sum = pre_sum[i][c2] - (pre_sum[i][c1-1] if c1 > 0 else 0)
                    cur_arr.append(row_sum)

                ans += getSubArrCountWithTarget(cur_arr)

        return ans
