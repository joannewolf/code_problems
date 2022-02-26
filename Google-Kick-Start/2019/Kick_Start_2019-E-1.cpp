// Cherries Mesh
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edb/0000000000170721

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N, M;
        cin >> N >> M;
        vector< set<int> > graph(N);
        for (int i = 0; i < M; i++) {
            int c, d;
            cin >> c >> d;
            graph[c - 1].insert(d - 1);
            graph[d - 1].insert(c - 1);
        }
        
        set<int> unchecked;
        for (int i = 0; i < N; i++) {
            unchecked.insert(i);
        }
        int group_count = 0;
        while (!unchecked.empty()) {
            set<int> queue;
            queue.insert(*unchecked.begin());
            while (!queue.empty()) {
                int v = *queue.begin();
                queue.erase(v);
                unchecked.erase(v);
                for (auto w : graph[v]) {
                    if (unchecked.find(w) != unchecked.end()) {
                        queue.insert(w);
                    }
                }
            }
            group_count += 1;
        }

        int result = (group_count - 1) * 2 + (N - group_count);
        printf("Case #%d: %d\n", t + 1, result);
    }
}
