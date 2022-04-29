// Sightseeing
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201b77/0000000000201bfd
// DP, TLE but correct locally on test set 2

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll INF = pow(10, 10);

ll N, T_S, T_F;
vector< vector<ll> > bus;
map< pair<ll, int>, ll> dp;

// The max # of sightseeing if reach city i at sec start
ll go(ll start, int i) {
    if (i == N - 1) {
        if (start > T_F)
            return -INF;
        else
            return 0;
    }

    pair<ll, int> key = make_pair(start, i);
    if (dp.find(key) != dp.end()) {
        return dp[key];
    }
    
    // Go without sightseeing city i
    int x = max((int)ceil((double)(start - bus[i][0]) / bus[i][1]), 0);
    ll option1 = go(bus[i][0] + x * bus[i][1] + bus[i][2], i + 1);
    // Go with sightseeing city i
    x = max((int)ceil((double)(start + T_S - bus[i][0]) / bus[i][1]), 0);
    ll option2 = 1 + go(bus[i][0] + x * bus[i][1] + bus[i][2], i + 1);

    dp[key] = max(option1, option2);
    return dp[key];

}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        cin >> N >> T_S >> T_F;
        bus.clear();
        dp.clear();
        for (int i = 0; i < N - 1; i++) {
            vector<ll> temp(3);
            cin >> temp[0] >> temp[1] >> temp[2];
            bus.push_back(temp);
        }

        ll ans = go(0, 0);
        if (ans < 0)
            printf("Case #%d: IMPOSSIBLE\n", t + 1);
        else
            printf("Case #%d: %lld\n", t + 1, ans);
    }
}
