// Paragliding
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee1/0000000000051006
// O((N+K)logN)

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N, K;
        ll p1, p2, A1, B1, C1, M1;
        ll h1, h2, A2, B2, C2, M2;
        ll x1, x2, A3, B3, C3, M3;
        ll y1, y2, A4, B4, C4, M4;
        cin >> N >> K;
        cin >> p1 >> p2 >> A1 >> B1 >> C1 >> M1;
        cin >> h1 >> h2 >> A2 >> B2 >> C2 >> M2;
        cin >> x1 >> x2 >> A3 >> B3 >> C3 >> M3;
        cin >> y1 >> y2 >> A4 >> B4 >> C4 >> M4;

        vector<ll> P, H, X, Y;
        P.push_back(p1);
        P.push_back(p2);
        H.push_back(h1);
        H.push_back(h2);
        X.push_back(x1);
        X.push_back(x2);
        Y.push_back(y1);
        Y.push_back(y2);
        for (int i = 2; i < N; i++) {
            ll next_p = (P[i-1] * A1 + P[i-2] * B1 + C1) % M1 + 1;
            P.push_back(next_p);
            ll next_h = (H[i-1] * A2 + H[i-2] * B2 + C2) % M2 + 1;
            H.push_back(next_h);
        }
        for (int i = 2; i < K; i++) {
            ll next_x = (X[i-1] * A3 + X[i-2] * B3 + C3) % M3 + 1;
            X.push_back(next_x);
            ll next_y = (Y[i-1] * A4 + Y[i-2] * B4 + C4) % M4 + 1;
            Y.push_back(next_y);
        }

        // Optimization idea: if H[i] <= H[j] - abs(P[i] - P[j]), means any balloon reachable by i can be also reached by j
        // So remove those towers which can be covered by others
        // O(NlogN + N)
        vector< pair<ll, ll> > towers, key_towers;
        for (int i = 0; i < N; i++)
            towers.push_back(make_pair(P[i], H[i]));
        sort(towers.begin(), towers.end());

        int flag = 0;
        while (flag < N) {
            if (!key_towers.empty() && towers[flag].second <= key_towers.back().second - abs(towers[flag].first - key_towers.back().first)) {
                flag += 1;
            }
            else {
                while (!key_towers.empty()) {
                    if (key_towers.back().second <= towers[flag].second - abs(towers[flag].first - key_towers.back().first))
                        key_towers.pop_back();
                    else
                        break;
                }
                key_towers.push_back(towers[flag]);
            }

        }

        // After tower optimization, for each balloon, if it can be collected, it must be the closest tower
        // Use binary search to find the closest tower of each balloon
        // O(KlogN)
        int ans = 0;
        int N2 = key_towers.size();
        for (int i = 0; i < K; i++) {
            int l = 0, r = N2 - 1;
            while (l <= r) {
                int mid = (l + r) / 2;
                if (key_towers[mid].first <= X[i])
                    l = mid + 1;
                else
                    r = mid - 1;
            }

            // final R is max element index which <= target
            // final L is min element index which > target
            if (r == -1) { // Balloon is on left side of all towers
                if (key_towers[0].second >= Y[i] + (key_towers[0].first - X[i]))
                    ans += 1;
            }
            else if (l == N2) { // Balloon is on right side of all towers
                if (key_towers.back().second >= Y[i] + (X[i] - key_towers.back().first))
                    ans += 1;
            }
            else {
                if (key_towers[l].second >= Y[i] + (key_towers[l].first - X[i]) ||
                    key_towers[r].second >= Y[i] + (X[i] - key_towers[r].first))
                    ans += 1;
            }
        }
        printf("Case #%d: %lld\n", t + 1, ans);
    }
}
