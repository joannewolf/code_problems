// Sherlock and Matrix Game
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201b77/0000000000201c95
// O(N^4*logK), TLE on test set 2

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N, K, A1, B1, C, D, E1, E2, F;
        cin >> N >> K >> A1 >> B1 >> C >> D >> E1 >> E2 >> F;
        vector<int> A, B;
        A.push_back(A1);
        B.push_back(B1);
        int x = A1, y = B1, r = 0, s = 0;
        for (int i = 1; i < N; i++) {
            int new_x = (C * x + D * y + E1) % F;
            int new_y = (D * x + C * y + E2) % F;
            int new_r = (C * r + D * s + E1) % 2;
            int new_s = (D * r + C * s + E2) % 2;
            A.push_back(pow(-1, new_r) * new_x);
            B.push_back(pow(-1, new_s) * new_y);
            x = new_x;
            y = new_y;
            r = new_r;
            s = new_s;
        }

        vector<ll> prefix_A, prefix_B;
        prefix_A.push_back(0);
        prefix_B.push_back(0);
        for (int i = 0; i < N; i++) {
            prefix_A.push_back(prefix_A.back() + A[i]);
            prefix_B.push_back(prefix_B.back() + B[i]);
        }

        priority_queue<ll, vector<ll>, greater<ll> > pq; // Priority queue of top-K element
        // submatrix of row [i1, j1] and column [i2, j2], inclusive
        for (int i1 = 0; i1 < N; i1++) {
            for (int j1 = i1; j1 < N; j1++) {
                for (int i2 = 0; i2 < N; i2++) {
                    for (int j2 = i2; j2 < N; j2++) {
                        ll temp = (prefix_A[j1+1] - prefix_A[i1]) * (prefix_B[j2+1] - prefix_B[i2]);
                        if (pq.size() < K)
                            pq.push(temp);
                        else if (pq.top() < temp) {
                            pq.pop();
                            pq.push(temp);
                        }
                    }
                }
            }
        }

        printf("Case #%d: %lld\n", t + 1, pq.top());
    }
}
