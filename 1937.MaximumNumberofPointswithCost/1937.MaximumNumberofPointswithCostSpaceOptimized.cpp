/*
Space optimized solution that removes the previous temporary arrays
leftToRight and rightToLeft, opting to use dp[] for all operations instead
O(m * n) time complexity
O(n) space complexity
*/
class Solution {
public:
  long long maxPoints(vector<vector<int>>& points) {
    int m = points.size(), n = points[0].size();
    vector<long long> dp(n, 0);
    for(int i = m - 1; i >= 0; i--) {
      for(int j = 1; j < n; j++) {
        dp[j] = max(dp[j - 1] - 1, dp[j]);
        dp[n - 1 - j] = max(dp[n - j] - 1, dp[n - 1 - j]);
      }
      for(int j = 0; j < n; j++)
        dp[j] += points[i][j];
    }
    long long ans = 0;
    for(int j = 0; j < n; j++)
      ans = max(ans, dp[j]);
    return ans;
  }
