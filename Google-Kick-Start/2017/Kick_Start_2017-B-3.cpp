// Christmas Tree
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201d27/0000000000201c9a
// DP, O(NMK*NM)

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll MIN_INT = -pow(10, 9);

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N, M, K;
        cin >> N >> M >> K;
        vector<string> grid(N);
        for (int i = 0; i < N; i++) {
            cin >> grid[i];
        }

        vector< vector<int> > prefix(N, vector<int>(1, 0));
        // prefix[i][j]: # of greens between grid[i][0] ~ grid[i][j], inclusive
        vector< vector< vector<ll> > > dp(N+1, vector< vector<ll> >(M, vector<ll>(K+1, MIN_INT)));
        // dp[i][j][k]: the max # of greens of k-tree starting at grid[i][j]
        for (int i = 0; i <= N; i++) {
            for (int j = 0; j < M; j++) {
                dp[i][j][0] = 0;
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                prefix[i].push_back(prefix[i].back() + (grid[i][j] == '#'));
            }
        }

        for (int k = 1; k <= K; k++) {
            for (int i = N - 1; i >= 0; i--) {
                for (int j = 0; j < M; j++) {
                    if (grid[i][j] == '#') {
                        for (int level = 0; level < N - i; level++) {
                            int row = i + level;
                            int l = j - level, r = j + level;
                            if (l < 0 || r >= M || prefix[row][r+1] - prefix[row][l] != r - l + 1)
                                break;
                            ll tree = (level + 1) * (level + 1);
                            for (int x = l; x <= r; x++)
                                dp[i][j][k] = max(dp[i][j][k], tree + dp[row + 1][x][k - 1]);
                        }
                    }
                }
            }
        }

        ll ans = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                ans = max(ans, dp[i][j][K]);
            }
        }
        
        printf("Case #%d: %lld\n", t + 1, ans);
    }
}
