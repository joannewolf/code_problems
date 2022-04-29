// Sightseeing
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201b77/0000000000201bfd
// DP, O(N^2)

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll INF = pow(10, 10);

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        ll N, T_S, T_F;
        cin >> N >> T_S >> T_F;
        vector< vector<ll> > bus;
        for (int i = 0; i < N - 1; i++) {
            vector<ll> temp(3);
            cin >> temp[0] >> temp[1] >> temp[2];
            bus.push_back(temp);
        }

        vector< vector<ll> > dp(N, vector<ll>(N, INF));
        // dp[i][j]: the min time to reach city i while sightseeing j cities
        dp[0][0] = 0;
        for (int i = 1; i < N; i++) {
            int x;
            x = max((int)ceil((double)(dp[i - 1][0] - bus[i-1][0]) / bus[i-1][1]), 0);
            dp[i][0] = bus[i-1][0] + x * bus[i-1][1] + bus[i-1][2];

            for (int j = 1; j < i; j++) {
                x = max((int)ceil((double)(dp[i - 1][j] - bus[i-1][0]) / bus[i-1][1]), 0);
                ll option1 = bus[i-1][0] + x * bus[i-1][1] + bus[i-1][2];
                x = max((int)ceil((double)(dp[i - 1][j - 1] + T_S - bus[i-1][0]) / bus[i-1][1]), 0);
                ll option2 = bus[i-1][0] + x * bus[i-1][1] + bus[i-1][2];
                dp[i][j] = min(option1, option2);
            }

            x = max((int)ceil((double)(dp[i - 1][i - 1] + T_S - bus[i-1][0]) / bus[i-1][1]), 0);
            dp[i][i] = bus[i-1][0] + x * bus[i-1][1] + bus[i-1][2];
        }

        int ans = -1;
        for (int j = 0; j < N; j++) {
            if (dp[N-1][j] <= T_F)
                ans = j;
        }
        if (ans == -1)
            printf("Case #%d: IMPOSSIBLE\n", t + 1);
        else
            printf("Case #%d: %d\n", t + 1, ans);
    }
}
