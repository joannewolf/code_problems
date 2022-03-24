// Candies
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee1/00000000000510ef
// Key idea: If for l', r' is the rightmost index which satisfying odd[l', r'] <= O, then odd[l'+1, r'] <= O must also satisfy
// For test set 1 only, L = 0, all Si >= 0, if r' also satisfying sum[l', r'] <= D, sum[l'+1, r'] <= D must also satisfy

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll N_INF = -pow(10, 15) - 1;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N, O, X1, X2, A, B, C, M, L;
        ll D;
        cin >> N >> O >> D;
        cin >> X1 >> X2 >> A >> B >> C >> M >> L;

        vector<ll> S;
        S.push_back(X1);
        S.push_back(X2);
        for (int i = 2; i < N; i++) {
            ll next = (S[i-1] * A + S[i-2] * B + C) % M;
            S.push_back(next);
        }
        for (int i = 0; i < N; i++)
            S[i] += L;
        // for (int i = 0; i < N; i++)
        //     printf("%lld ", S[i]);
        // printf("\n");

        vector<ll> sum;
        vector<int> odd;
        sum.push_back(0);
        odd.push_back(0);
        for (int i = 0; i < N; i++) {
            sum.push_back(sum.back() + S[i]);
            odd.push_back(odd.back() + abs(S[i] % 2));
        }
        // for (int i = 0; i <= N; i++)
        //     printf("%lld ", sum[i]);
        // printf("\n");
        // for (int i = 0; i <= N; i++)
        //     printf("%d ", odd[i]);
        // printf("\n");

        ll ans = N_INF;

        // O(N), Only handle test set 1, L = 0 -> all Si >= 0
        // For each l, the rightmost index which satisfying constraints will always give maximized sum
        // So for next l, we can start iterate from last rightmost index
        // int flag_r = 0;
        // for (int l = 0; l < N; l++) {
        //     for (int r = flag_r; r <= N; r++) {
        //         if (r == N || odd[r+1] - odd[l] > O || sum[r+1] - sum[l] > D) {
        //             flag_r = r;
        //             break;
        //         }
        //     }
        //     if (flag_r > l && sum[flag_r] - sum[l] > ans) {
        //         ans = sum[flag_r] - sum[l];
        //     }
        // }

        // For test set 2, instead of directly taking the rightmost index, we search all candidates within rightmost index and get the one which satifying sum[l, r'] <= D
        // We need a data structure for candidates, it should support adding int, removing int, and finding the max int which <= target
        // Binary search tree can do it, O(NlogN)
        int flag_r = 0;
        multiset<ll> candidates;
        for (int l = 0; l < N; l++) {
            for (int r = max(l, flag_r); r <= N; r++) {
                if (r == N || odd[r+1] - odd[l] > O) {
                    flag_r = r;
                    break;
                }
                else {
                    candidates.insert(sum[r+1]);
                }
            }
            // Find max candidate - sum[l] <= D
            // upper_bound(): return first item > target
            auto it = candidates.upper_bound(D + sum[l]);
            if (it != candidates.begin()) {
                it--;
                if (*it - sum[l] > ans) {
                    ans = *it - sum[l];
                }
            }

            it = candidates.find(sum[l+1]);
            if (it != candidates.end())
                candidates.erase(it);
        }
        
        if (ans == N_INF)
            printf("Case #%d: IMPOSSIBLE\n", t + 1);
        else
            printf("Case #%d: %lld\n", t + 1, ans);
    }
}
