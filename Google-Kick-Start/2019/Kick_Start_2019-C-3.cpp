// Catch Some
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff2/0000000000150a0d
// The problem can be transform to:
// Within C different colors of dogs, let's say we choose k_i dogs for color i
// Find SUM(k_i) = K, and minimum time = dogs[1][k_1] * 2 + ... + dogs[C][k_C]
// For the last color we choose, we don't need to go back home so no need multipled by 2
// The reason is:
// (1) We don't change to the color that we observe before, cuz that's not optimal
// (2) If we choose to observe color i's j-th dog, it's optimal that we will also observe all dogs before j-th
// (3) The order of color doesn't matter
// DP, O(N^2)

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N, K;
        cin >> N >> K;
        vector<int> P(N), A(N);
        for (int i = 0; i < N; i++)
            cin >> P[i];
        for (int i = 0; i < N; i++)
            cin >> A[i];

        map<int, vector<int> > temp;
        for (int i = 0; i < N; i++) {
            if (temp.find(A[i]) == temp.end())
                temp[A[i]] = vector<int>(1, P[i]);
            else
                temp[A[i]].push_back(P[i]);
        }
        vector< vector<int> > dogs;
        for (auto &dog : temp) {
            sort(dog.second.begin(), dog.second.end());
            dogs.push_back(dog.second);
        }
        int C = dogs.size();
        
        vector< vector< vector<ll> > > dp(C+1, vector< vector<ll> >(K+1, vector<ll>(2, pow(10, 9))));
        // dp[i][j][k]: The min time to observe j dogs with first i colors, k is 0/1 denoting whether decided the last color
        for (int i = 0; i <= C; i++) {
            dp[i][0][0] = 0;
            dp[i][0][1] = 0;
        }

        for (int i = 1; i <= C; i++) {
            int L = dogs[i-1].size(); // The # of dogs of current color
            for (int j = 1; j <= K; j++) {
                // Observe 0 dog of current color
                ll min_value1 = dp[i-1][j][0] + 2 * 0;
                ll min_value2 = dp[i-1][j][0] + 0;
                ll min_value3 = dp[i-1][j][1] + 2 * 0;
                // Observe 1...L dogs of current color
                for (int l = 0; l < min(L, j); l++) {
                    min_value1 = min(min_value1, dp[i-1][j-l-1][0] + 2 * dogs[i-1][l]);
                    min_value2 = min(min_value2, dp[i-1][j-l-1][0] + dogs[i-1][l]); // Take current color as last color
                    min_value3 = min(min_value3, dp[i-1][j-l-1][1] + 2 * dogs[i-1][l]); // Already decide last color before
                }
                dp[i][j][0] = min_value1;
                dp[i][j][1] = min(min_value2, min_value3);
            }
        }
        printf("Case #%d: %lld\n", t + 1, dp[C][K][1]);
    }
}
