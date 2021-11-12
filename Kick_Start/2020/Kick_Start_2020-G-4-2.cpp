// Merge Cards
// https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000415054
// Optimize the DP solution, O(N^2)

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N;
        cin >> N;
        vector<ll> nums(N);
        for (int i = 0; i < N; i++)
            cin >> nums[i];

        vector<double> num_sum(N + 1, 0); // i < j, nums[i] ~ nums[j] = num_sum[j + 1] - num_sum[i]
        for (int i = 0; i < N; i++)
            num_sum[i + 1] = num_sum[i] + nums[i];
        // dp[i][j]: the expected value to construct nums[i]~nums[j], inclusive
        vector<double> prefix_sum(N, 0); // prefix_sum[i]: sum(dp[i][i] ~ dp[i][current])
        vector<double> suffix_sum(N, 0); // suffix_sum[i]: sum(dp[i][current] ~ dp[i][i])

        double ans;
        for (int i = 1; i < N; i++) {
            for (int start = 0; start < N - i; start++) {
                // Calculate dp[start][start + i]
                double temp_sum = (prefix_sum[start] + suffix_sum[start + i]) / i + (num_sum[start + i + 1] - num_sum[start]);
                ans = temp_sum;
                prefix_sum[start] += temp_sum;
                suffix_sum[start + i] += temp_sum;
            }
        }
        
        printf("Case #%d: %f\n", t + 1, ans);
    }
}
