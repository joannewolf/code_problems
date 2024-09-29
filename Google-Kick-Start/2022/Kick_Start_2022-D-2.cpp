// Maximum Gain
// https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76fae

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll MAX_INT = pow(10, 14);

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N, M, K;
        vector<ll> A, B;
        cin >> N;
        A.reserve(N);
        for (int i = 0; i < N; i++)
            cin >> A[i];
        cin >> M;
        B.reserve(M);
        for (int i = 0; i < M; i++)
            cin >> B[i];
        cin >> K;

        int K2 = N + M - K;
        vector<ll> prefix_A, prefix_B;
        prefix_A.push_back(0);
        prefix_B.push_back(0);
        for (int i = 0; i < N; i++)
            prefix_A.push_back(prefix_A.back() + A[i]);
        for (int i = 0; i < M; i++)
            prefix_B.push_back(prefix_B.back() + B[i]);

        // Find min subarray sum in A and B, and the two subarray length sum be (N + M - K)
        ll ans = MAX_INT;

        for (int i = max(0, K2 - M); i <= min(N, K2); i++) {
            // Use subarray len i in A, and subarray len j in B, find the min subarray value respectively
            int j = K2 - i;
            ll min_A = MAX_INT, min_B = MAX_INT;
            for (int l = 0; l <= N - i; l++) {
                int r = l + i;
                min_A = min(min_A, prefix_A[r] - prefix_A[l]);
            }
            for (int l = 0; l <= M - j; l++) {
                int r = l + j;
                min_B = min(min_B, prefix_B[r] - prefix_B[l]);
            }

            if (i == 0)
                min_A = 0;
            if (j == 0)
                min_B = 0;

            ans = min(ans, min_A + min_B);
        }
        ans = prefix_A.back() + prefix_B.back() - ans;
        
        printf("Case #%d: %lld\n", t + 1, ans);
    }
}
