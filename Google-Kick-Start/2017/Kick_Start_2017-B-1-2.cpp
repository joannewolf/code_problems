// Math Encoder
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201d27/0000000000201b7b
// Different instances of same number are taken as different, e.g. nums = [1, 2, 3, 3], there will be 2 subsets of [1, 2, 3]

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll MOD = pow(10, 9) + 7;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N;
        cin >> N;
        vector<int> nums(N);
        for (int i = 0; i < N; i++) {
            cin >> nums[i];
        }

        ll ans = 0;
        ll pow2 = 1;
        for (int gap = 1; gap < N; gap++) {
            for (int i = 0; i < N - gap; i++) {
                int j = i + gap;
                ans += (nums[j] - nums[i]) * pow2 % MOD;
                ans %= MOD;
            }
            pow2 = pow2 * 2 % MOD;
        }

        printf("Case #%d: %lld\n", t + 1, ans);
    }
}
