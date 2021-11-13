// Friends
// https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043aee7
// Use Floyd–Warshall algorithm to find all pair of shortest paths between letters
// O(L^2*N + 26^3 + L^2*Q) = O(L^2*(N+Q))

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int INF = pow(10, 5);
int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N, Q;
        cin >> N >> Q;
        vector<string> names(N);
        for (int i = 0; i < N; i++)
            cin >> names[i];

        vector< vector<int> > dist(26, vector<int>(26, INF));
        for (int i = 0; i < 26; i++)
            dist[i][i] = 0;
        // Letters have edge only if they appear in same name
        for (int i = 0; i < N; i++) {
            for (char c1: names[i]) {
                for (char c2: names[i]) {
                    if (c1 != c2) {
                        dist[c1 - 'A'][c2 - 'A'] = 1;
                        dist[c2 - 'A'][c1 - 'A'] = 1;
                    }
                }
            }
        }
        for (int k = 0; k < 26; k++) {
            for (int i = 0; i < 26; i++) {
                for (int j = 0; j < 26; j++) {
                    if (dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
        
        printf("Case #%d:", t + 1);
        for (int i = 0; i < Q; i++) {
            int x, y;
            cin >> x >> y;
            int ans = INF;
            for (char c1: names[x - 1]) {
                for (char c2: names[y - 1]) {
                    ans = min(ans, dist[c1 - 'A'][c2 - 'A']);
                }
            }
            if (ans != INF)
            // ans: # of edge in letter's graph, means there are ans + 1 letters are used to connect, means there are ans + 2 people in chain
                printf(" %d", ans + 2);
            else
                printf(" -1");
        }
        printf("\n");
    }
}
