// X or What?
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051061/0000000000161426
// odd_bit XOR odd_bit = even_bit
// odd_bit XOR even_bit = odd_bit
// even_bit XOR even_bit = even_bit
// So the problem can be transform to:
// If there are even number of odd_bit, whole array is xor-even; else, it will be the subinterval without first or last odd_bit
// If using ordered data structure, O((N+Q)logN)

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

bool is_odd_bit(int num) {
    int count = 0;
    while (num != 0) {
        count += num % 2;
        num >>= 1;
    }
    return count % 2;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N, Q, num;
        cin >> N >> Q;
        set<int> odd_bit;
        for (int i = 0; i < N; i++) {
            cin >> num;
            if (is_odd_bit(num))
                odd_bit.insert(i);
        }

        printf("Case #%d:", t + 1);
        for (int i = 0; i < Q; i++) {
            int p, v;
            cin >> p >> v;

            if (is_odd_bit(v))
                odd_bit.insert(p);
            else
                odd_bit.erase(p);

            int ans = 0;
            if (odd_bit.size() % 2 == 1) {
                ans = max(ans, N - *odd_bit.begin() - 1);
                ans = max(ans, *odd_bit.rbegin());
            }
            else
                ans = N;
            printf(" %d", ans);
        }
        printf("\n");
    }
}
