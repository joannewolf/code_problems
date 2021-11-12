// Combination Lock
// https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a24
// Sort initial values, and for each Xi find index 1 <= p <= i and i <= b <= W, such that distance can be calculated as below
// 1---------p-------i-------b---------W
//   N-Xi+Xr   Xi-Xq   Xc-Xi   N-Xd+Xi
// Xp = Xi - N / 2, Xb = Xi + N / 2
// p and b can be found in O(logW) using binary search, and sum(distance to Xi) can be found in O(1) with prefix sum array
// O(WlogW)

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

vector<ll> prefix_sum;

// Sum of subarray X[l] ~ X[r], inclusive
ll get_sum(int l, int r) {
    if (l <= r) {
        if (l <= 0)
            return prefix_sum[r];
        else
            return prefix_sum[r] - prefix_sum[l - 1];
    }
    else
        return 0;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int W, N;
        cin >> W >> N;
        vector<ll> X(W);
        for (int i = 0; i < W; i++)
            cin >> X[i];
        sort(X.begin(), X.end());

        prefix_sum = vector<ll>(W, 0);
        prefix_sum[0] = X[0];
        for (int i = 1; i < W; i++)
            prefix_sum[i] = prefix_sum[i - 1] + X[i];

        ll ans = LLONG_MAX;
        for (int i = 0; i < W; i++) {
            ll sum = 0;
            int l, r;
            // Find the min index which Xi - X* > N - Xi + X*
            l = 0;
            r = i;
            while (l <= r) {
                int mid = l + (r - l) / 2;
                ll diff = X[i] - X[mid];
                if (diff > (ll)N - diff)
                    l = mid + 1;
                else
                    r = mid - 1;
            }
            // index l ~ i use Xi-X
            sum += (i - l + 1) * X[i] - get_sum(l, i);
            // index 0 ~ l - 1 use N-Xi+X, 
            sum += l * (N - X[i]) + get_sum(0, l - 1);

            // Find the max index which X* - Xi > N - X* + Xi
            l = i;
            r = W - 1;
            while (l <= r) {
                int mid = l + (r - l) / 2;
                ll diff = X[mid] - X[i];
                if (diff > N - diff)
                    r = mid - 1;
                else
                    l = mid + 1;
            }
            // index i ~ r use X-Xi
            sum += get_sum(i, r) - (r - i + 1) * X[i];
            // index r + 1 ~ W - 1 use N-X+Xi, 
            sum += (W - r - 1) * (N + X[i]) - get_sum(r + 1, W - 1);

            ans = min(ans, sum);
        }
        printf("Case #%d: %lld\n", t + 1, ans);
    }
}
