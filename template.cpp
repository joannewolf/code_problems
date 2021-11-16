// 
// https://codingcompetitions.withgoogle.com/

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int M;
        cin >> M;
        vector< pair<long long, long long> > employees;
        vector< vector<int> > dist(26, vector<int>(26, LLONG_MAX));
        for (int j = 0; j < L; j++) {
            cin >> num;
            cin >> level;
            employees.push_back(make_pair(level, num));
        }
        
        printf("Case #%d: %lld\n", t + 1, result);
    }
}
