// Matrix Cutting
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201b7d/0000000000201d2b
// DP, O(N^2*M^2(N+M))

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll INF = pow(10, 10);

vector< vector<ll> > grid;
vector< vector< vector< vector<ll> > > > dp;
// dp[i1][i2][j1][j2]: the result of cutting submatrices grid[i1~i2][j1~j2], inclusive
// 0 <= i1, i2 < N; 0 <= j1, j2 < M

ll solve(int i1, int i2, int j1, int j2) {
    if (dp[i1][i2][j1][j2] != -1) {
        return dp[i1][i2][j1][j2];
    }

    if (i1 == i2 && j1 == j2) {
        dp[i1][i2][j1][j2] = 0;
        return 0;
    }

    // Find the min value of current submatrice
    ll min_value = INF;
    for (int i = i1; i <= i2; i++) {
        for (int j = j1; j <= j2; j++)
            min_value = min(min_value, grid[i][j]);
    }

    ll submatrices = 0;
    // Cut horizontally
    for (int gap_i = 0; gap_i < i2 - i1; gap_i++) {
        submatrices = max(submatrices, solve(i1, i1 + gap_i, j1, j2) + solve(i1 + gap_i + 1, i2, j1, j2));
    }
    // Cut vertically
    for (int gap_j = 0; gap_j < j2 - j1; gap_j++) {
        submatrices = max(submatrices, solve(i1, i2, j1, j1 + gap_j) + solve(i1, i2, j1 + gap_j + 1, j2));
    }

    dp[i1][i2][j1][j2] = min_value + submatrices;
    return dp[i1][i2][j1][j2];
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N, M;
        cin >> N >> M;
        grid.clear();
        dp.clear();

        for (int i = 0; i < N; i++) {
            vector<ll> row(M);
            for (int j = 0; j < M; j++)
                cin >> row[j];
            grid.push_back(row);
        }

        vector< vector< vector< vector<ll> > > > new_dp(N, vector< vector< vector<ll> > >(N, vector< vector<ll> >(M, vector<ll>(M, -1))));
        dp = new_dp;

        printf("Case #%d: %lld\n", t + 1, solve(0, N-1, 0, M-1));
    }
}
