// 
// https://codingcompetitions.withgoogle.com/

#include <iostream>
#include <vector>
#include <utility>
#include <math.h>
#include <algorithm>
#include <set>

#define ll long long

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int M;
        cin >> M;
        vector< pair<long long, long long> > employees;
        for (int j = 0; j < L; j++) {
            cin >> num;
            cin >> level;
            employees.push_back(make_pair(level, num));
        }
        
        printf("Case #%d: %lld\n", t + 1, result);
    }
}
