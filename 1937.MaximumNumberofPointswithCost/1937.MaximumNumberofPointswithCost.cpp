/*Dynamic programming solution to leetcode 1937
 O(m * n) time complexity
 O(n) space complexity*/
class Solution {
public:
  long long maxPoints(vector<vector<int>>& points) {
    int m = points.size(), n = points[0].size();
    vector<long long> dp(n, 0);

    long long ans = 0;
    for(int i = m - 1; i >= 0; i--) {
      vector<long long> leftToRight(n), rightToLeft(n);
      leftToRight[0] = dp[0], rightToLeft[n - 1] = dp[n - 1];
      for(int j = 1; j < n; j++) {
      leftToRight[j] = max(leftToRight[j - 1] - 1, dp[j]);
      rightToLeft[n - 1 - j] = max(rightToLeft[n - j] - 1, dp[n - 1 -j]);
      }

    for (int j = 0; j < n; j++)
      dp[j] = points[i][j] + max(leftToRight[j], rightToLeft[j]);
  }

    for(int j = 0; j < n; j++)
      ans = max(ans, dp[j]);
      return ans;
  }
};
