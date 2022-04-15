// Pattern Overlap
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201c97/0000000000201b79

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

vector< vector<int> > match;
string S1, S2;
int N1, N2;

int solve(int flag1, int flag2) {
    // print("flag1", flag1, S1[flag1:], "flag2", flag2, S2[flag2:])
    if (match[flag1][flag2] != -1)
        return match[flag1][flag2];

    if (flag1 == N1) {
        int valid = 1;
        for (int i = flag2; i < N2; i++) {
            if (S2[i] != '*') {
                valid = 0;
                break;
            }
        }
        for (int i = flag2; i < N2; i++) {
            match[flag1][i] = valid;
        }
    }
    else if (flag2 == N2) {
        int valid = 1;
        for (int i = flag1; i < N1; i++) {
            if (S1[i] != '*') {
                valid = 0;
                break;
            }
        }
        for (int i = flag1; i < N1; i++) {
            match[i][flag2] = valid;
        }
    }
    else if (S1[flag1] != '*' && S2[flag2] != '*') {
        if (S1[flag1] == S2[flag2])
            match[flag1][flag2] = solve(flag1 + 1, flag2 + 1);
        else
            match[flag1][flag2] = 0;
    }
    else {
        int res = 0;
        if (S1[flag1] == '*') {
            int count_c2 = 0;
            for (int i = flag2; i <= N2; i++) {
                if (count_c2 <= 4) {
                    res |= solve(flag1 + 1, i);
                    if (res) {
                        match[flag1][flag2] = res;
                        break;
                    }
                }
                else
                    break;
                if (i != N2 && S2[i] != '*')
                    count_c2 += 1;
            }
        }
        if (S2[flag2] == '*') {
            int count_c1 = 0;
            for (int i = flag1; i <= N1; i++) {
                if (count_c1 <= 4) {
                    res |= solve(i, flag2 + 1);
                    if (res) {
                        match[flag1][flag2] = res;
                        break;
                    }
                }
                else
                    break;
                if (i != N1 && S1[i] != '*')
                    count_c1 += 1;
            }
        }
        match[flag1][flag2] = res;
    }

    return match[flag1][flag2];
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        S1.clear();
        S2.clear();
        cin >> S1 >> S2;
        N1 = S1.length();
        N2 = S2.length();

        match.clear();
        match.assign(N1+1, vector<int>(N2+1, -1));
        match[N1][N2] = 1;

        solve(0, 0);

        if (match[0][0] == 1)
            printf("Case #%d: TRUE\n", t + 1);
        else
            printf("Case #%d: FALSE\n", t + 1);
    }
}
