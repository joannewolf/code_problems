// Banana Bunches
// https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b44ef
// The problem can be translate to finding 2 non-overlapping interval (i, j), (x, y) and i <= j < x <= y
// Such that sum(B[i:j+1]) + sum(B[x:y+1]) = K and j - i + 1 + y - x + 1 is minimum
// Store the optimal length of second subarray for each sum, then iterate all pair of (i, j)
// O(N^2)

#include <iostream>
#include <vector>
#include <utility>
#include <math.h>
#include <algorithm>
#include <set>

#define ll long long

using namespace std;

ll MAX_INT = pow(10, 7);
int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N, K;
        cin >> N >> K;
        vector<ll> B;
        for (int i = 0; i < N; i++) {
            ll b;
            cin >> b;
            B.push_back(b);
        }

        if (find(B.begin(), B.end(), K) != B.end()) {
            printf("Case #%d: 1\n", t + 1);
            continue;
        }

        ll result = MAX_INT;
        vector<ll> best(K + 1, MAX_INT);
        for (int j = N - 1; j >= 0; j--) {
            ll temp_sum = 0; // sum of B[i] ~ B[j]
            for (int i = j; i >= 0; i--) {
                temp_sum += B[i];
                if (temp_sum <= K)
                    result = min(result, j - i + 1 + best[K - temp_sum]);
            }

            // Grow second subarray from small to big
            ll temp_sum_2 = 0; // sum of B[j] ~ B[x]
            for (int x = j; x < N; x++) {
                temp_sum_2 += B[x];
                if (temp_sum_2 <= K)
                    best[temp_sum_2] = min(best[temp_sum_2], (ll)(x - j + 1));
            }
        }

        if (result == MAX_INT)
            printf("Case #%d: -1\n", t + 1);
        else
            printf("Case #%d: %lld\n", t + 1, result);
    }
}
