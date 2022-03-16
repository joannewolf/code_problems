// Sherlock and the Bit Strings
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff4/000000000005107b
// Key idea: count the # of valid string given prefix and the input constraints
// Then we can fill the bits one by one (choose bit 0 first), if the prefix count >= P, then final result is within it, otherwise choose bit 1
// To get all the prefix count, use DP, define dp[i][j], i = 1~N, j = 0~2^16, means
//   The prefix is fixed until i-th bit, no matter what i - 16 bit and before are
//   The last 16 bits are as j (cuz constraints B - A >= 15, at most 16 bits)
//   This assignment satisfys all constraints where B >= i
// O(2^16 * N * K)

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll MAX_P = pow(10, 18) + 1;
int MASK = (1 << 16) - 1; // 1111111111111111, 16 1's, for taking only last 16 bits
int M = (1 << 16);
vector<int> one_count(M, 0);

bool pass_constraints(int bits, int b, vector<pair<int, int> > constraints) {
    for (auto p : constraints) {
        // Take only last n bits and count how many 1's
        if (one_count[bits & ((1 << p.first) - 1)] != p.second)
            return false;
    }
    return true;
}

ll add(ll a, ll b) {
    if (a == MAX_P || b == MAX_P)
        return MAX_P;
    else
        return min(a + b, MAX_P);
}

int main() {

    for (int i = 0; i < M; i++)
        one_count[i] = one_count[i >> 1] + (i & 1);

    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N, K;
        ll P;
        cin >> N >> K >> P;
        vector< vector<pair<int, int> > > constraints(N, vector<pair<int, int> >());
        for (int i = 0; i < K; i++) {
            int a, b, c;
            cin >> a >> b >> c;
            constraints[b - 1].push_back(make_pair(b - a + 1, c));
        }

        vector<vector<ll> > dp(N, vector<ll>(M, 0));
        for (int bits = 0; bits < M; bits++) {
            if (pass_constraints(bits, N - 1, constraints[N - 1])) {
                dp[N - 1][bits] = 1;
            }
        }
        for (int i = N - 2; i >= 0; i--) {
            for (int bits = 0; bits < M; bits++) {
                if (pass_constraints(bits, i, constraints[i])) {
                    int next = (bits << 1) & MASK;
                    dp[i][bits] = add(dp[i+1][next], dp[i+1][next|1]);
                }
            }
        }


        string ans = "";
        int last_bits = 0;
        for (int i = 0; i < N; i++) {
            // Append 0 as last bit, and ignore the first bit by applying mask
            int next = (last_bits << 1) & MASK;
            if (P <= dp[i][next]) { // If choose 0 as next bit have more than P results
                ans += "0";
                last_bits = next;
            }
            else {
                ans += "1";
                P -= dp[i][next];
                last_bits = next | 1; // Set last bit as 1
            }
        }
        printf("Case #%d: %s\n", t + 1, ans.c_str());
    }
}
