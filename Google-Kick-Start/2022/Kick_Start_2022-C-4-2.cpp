// Palindromic Deletions
// https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20d16
// Key idea: any panlindrome will be a subsequence of the input string S
// For a palindrome of length K, the # of games we will encounter it is (N - K)! * K!, first removing the unused char, then remove the used K char
// let f(K) = # of palindrome subsequence with len K, numerator = SUM{f(K) * (N - K)! * K!}, K = 0~N-1
// To find f(K), use DP
// O(N^3)

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll MOD = pow(10, 9) + 7;
int MAX_N = 400;

ll my_pow(ll a, ll b) {
    ll ans = 1;
    while (b) {
        if (b & 1)
            ans = ans * a % MOD;
        b >>= 1;
        a = a * a % MOD;
    }
    return ans;
}

int main() {
    vector<ll> fac(MAX_N + 1, 1);
    vector<ll> rfac(MAX_N + 1, 1);
    for (int i = 1; i <= MAX_N; i++)
        fac[i] = fac[i - 1] * (ll)i % MOD;
    rfac[MAX_N] = my_pow(fac[MAX_N], MOD - 2);
    for (int i = MAX_N - 1; i > 0; i--)
        rfac[i] = rfac[i + 1] * (ll)(i + 1) % MOD;

    // cout << fac[2] << " " << rfac[2] << " " << fac[2] * rfac[2] % MOD << endl;

    int T;
    cin >> T;
    
    for (int t = 0; t < T; t++) {
        int N;
        string S;
        cin >> N >> S;

        vector< vector< vector<ll> > > dp(N, vector< vector<ll> >(N, vector<ll>(N, 0)));
        // dp[l][r][k]: in substr S[l, r], inclusive, the # of palindrome subsequence of len k
        for (int l = 0; l < N; l++) {
            for (int r = 0; r < N; r++) {
                dp[l][r][0] = 1;
            }
        }

        for (int k = 1; k < N; k++) {
            for (int gap = k; gap <= N; gap++) {
                for (int l = 0; l <= N - gap; l++) {
                    int r = l + gap - 1;
                    if (l == r)
                        dp[l][r][k] = 1;
                    else {
                        ll temp = (dp[l][r-1][k] + dp[l+1][r][k]) % MOD;
                        temp -= dp[l+1][r-1][k];
                        if (temp < 0)
                            temp += MOD;
                        dp[l][r][k] = temp;
                        if (r > l && S[l] == S[r] && k >= 2)
                            dp[l][r][k] = (dp[l][r][k] + dp[l+1][r-1][k-2]) % MOD;
                    }
                }
            }
        }
        // for (int k = 0; k < N; k++) {
        //     printf("k %d\n", k);
        //     for (int l = 0; l < N; l++) {
        //         for (int r = 0; r < N; r++)
        //             printf("%lld ", dp[l][r][k]);
        //         printf("\n");
        //     }
        // }

        ll ans = 0;
        for (int k = 0; k < N; k++) {
            ll temp = dp[0][N - 1][k] * fac[k] % MOD;
            temp = temp * fac[N - k] % MOD;
            ans = (ans + temp) % MOD;
        }
        ans = (ans * rfac[N]) % MOD;
        if (ans < 0)
            ans += MOD;

        printf("Case #%d: %lld\n", t + 1, ans);
    }
}

