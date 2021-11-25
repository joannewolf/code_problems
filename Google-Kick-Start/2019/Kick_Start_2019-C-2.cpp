// Circuit Board
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff2/0000000000150aae
// The problem can be divided into 2 subproblems
// Subproblem 1: For each starting point (r, c), find the max length to its right side such that max-and-min-element-diff <= K
//   Subproblem 1.1: Get range minimum and maximum for each row, which can be achieved by using sparse table, pre-processing O(ClogC) for each row, query O(1) => total O(RClogC)
//   Subproblem 1.2: Use binary search to find the max index such that max-and-min-element-diff <= K, O(logC) for each (r, c) => total O(RClogC)
//      Since max-and-min-element-diff is non-decreasing when it goes to array's right side
// Subproblem 2: For each starting column j, we have the max length for each row, find the largest rectangle of histogram
//   For each num, take it as height of rectangle, and look for the furthest left/right index it can reach
// O(R) for each column => total O(RC)
// Overall O(RClogC)

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int R, C, K;
        cin >> R >> C >> K;
        vector< vector<int> > board;
        for (int i = 0; i < R; i++) {
            vector<int> row(C, 0);
            for (int j = 0; j < C; j++) {
                cin >> row[j];
            }
            board.push_back(row);
        }

        vector< vector<int> > histogram(R, vector<int>(C, 0)); // histogram[i][j]: on row i, the max length to board[i][j]'s right side such that max-and-min-element-diff <= K
        int LOG_C = floor(log2((double)C));

        for (int r = 0; r < R; r++) {
            // Subproblem 1.1 For each row, pre-process sparse tables for range min/max
            vector< vector<int> > sparse_min(C, vector<int>(LOG_C+1, 0));
            vector< vector<int> > sparse_max(C, vector<int>(LOG_C+1, 0));
            for (int c = 0; c < C; c++) {
                sparse_min[c][0] = board[r][c];
                sparse_max[c][0] = board[r][c];
            }
            for (int j = 1; j <= LOG_C; j++) {
                for (int i = 0; i < C - pow(2, j-1); i++) {
                    sparse_min[i][j] = min(sparse_min[i][j-1], sparse_min[i + pow(2, j-1)][j-1]);
                    sparse_max[i][j] = max(sparse_max[i][j-1], sparse_max[i + pow(2, j-1)][j-1]);
                }
            }
            // Subproblem 1.2
            for (int c = 0; c < C; c++) {
                int left = c, right = C-1;
                while (left <= right) {
                    int mid = (left + right) / 2;
                    int k = floor(log2((double)mid - c + 1));
                    int range_min = min(sparse_min[c][k], sparse_min[mid - pow(2, k) + 1][k]);
                    int range_max = max(sparse_max[c][k], sparse_max[mid - pow(2, k) + 1][k]);
                    if (range_max - range_min <= K)
                        left = mid + 1;
                    else
                        right = mid - 1;
                }
                // Final r is max element index which <= K
                histogram[r][c] = right - c + 1;
            }
        }
        //  Subproblem 2
        ll ans = 0;
        for (int c = 0; c < C; c++) {
            vector<int> left_bound(R, -1);
            vector<int> right_bound(R, -1);
            stack<int> st;

            // Find every num's right bound
            for (int r = 0; r < R; r++) {
                while (!st.empty() && histogram[st.top()][c] > histogram[r][c]) {
                    right_bound[st.top()] = r - 1;
                    st.pop();
                }
                st.push(r);
            }
            while (!st.empty()) {
                right_bound[st.top()] = R - 1;
                st.pop();
            }

            // Find every num's left bound
            for (int r = R-1; r >= 0; r--) {
                while (!st.empty() && histogram[st.top()][c] > histogram[r][c]) {
                    left_bound[st.top()] = r + 1;
                    st.pop();
                }
                st.push(r);
            }
            while (!st.empty()) {
                left_bound[st.top()] = 0;
                st.pop();
            }

            for (int r = 0; r < R; r++) {
                ans = max(ans, (ll)histogram[r][c] * (right_bound[r] - left_bound[r] + 1));
            }
        }

        printf("Case #%d: %lld\n", t + 1, ans);
    }
}
