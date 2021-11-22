// Merge Cards
// https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000415054
// Pre-compute the constant of A1, A2, ..., A_N, O(N^2) to compute all constants
// O(N) for each test to sum up the answer

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

vector< vector<double> > constant(2, vector<double>(0));

void expand_constant(int N) {
    for (int n = constant.size(); n <= N; n++) {
        vector<double> temp_constant(n, 0);
        // Iterate n - 1 types of merge, and multiply with previous constant
        for (int i = 0; i < n - 1; i++) {
            temp_constant[i] += 1;
            temp_constant[i + 1] += 1;
            for (int j = 0; j < i; j++)
                temp_constant[j] += constant.back()[j];
            temp_constant[i] += constant.back()[i];
            temp_constant[i + 1] += constant.back()[i];
            for (int j = i + 2; j < n; j++)
                temp_constant[j] += constant.back()[j - 1];
        }
        // Each merge are equally possible to occur, so expected value divided by n-1
        for (int i = 0; i < n; i++)
            temp_constant[i] /= (n - 1);
        constant.push_back(temp_constant);
    }
}

int main() {
    constant.push_back(vector<double>(2, 1.0));
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N;
        cin >> N;
        vector<ll> nums(N);
        for (int i = 0; i < N; i++)
            cin >> nums[i];

        if (N > constant.size() - 1)
            expand_constant(N);

        double ans = 0;
        for (int i = 0; i < N; i++)
            ans += constant[N][i] * nums[i];
        
        printf("Case #%d: %f\n", t + 1, ans);
    }
}
