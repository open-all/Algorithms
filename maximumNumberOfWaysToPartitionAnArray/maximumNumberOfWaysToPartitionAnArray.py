class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        presum = list(accumulate(nums))
        rightCnt = Counter()
        #the count of each original prefix - suffix on the right side of the current index,including current index
        leftCnt = Counter() # the count of each original prefix - suuffix on the left side of the current index, not including current index

        n = len(nums)

        for i in range (1,n):
            diff = presum[i - 1] - (presum[-1] - presum[i - 1])
            rightCnt[diff] += 1

        #if we don't change anything
        ans = rightCnt[0]

        #try to change each num
        for i in range(n):
            d = k - nums[i]

            ans = max(ans, leftCnt[d] + rightCnt[-d])

            if i < n - 1:
                origDiff = presum[i] - (presum[-1] - presum[i])
                leftCnt[origDiff] += 1
                rightCnt[origDiff] -= 1

        return ans
