// Weightlifting
// https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa9280
// Key idea: If there is a multiset which is common to all exercises, it's optimal to put them in the bottom of stacks
// If there's more than 1 exercise, there's at least one time that the stack only contains common weight multiset
// Then divide from that middle point, we can do the divide and conquer by dp
// O(E^2*W + E^3) = O(E^3)

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int MAX_INT = pow(10, 9);

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int E, W;
        cin >> E >> W;
        vector< vector<int> > exercises;
        for (int i = 0; i < E; i++) {
            vector<int> temp(W);
            for (int j = 0; j < W; j++) {
                cin >> temp[j];
            }
            exercises.push_back(temp);
        }

        vector< vector<int> > common(E, vector<int>(E, 0));
        // common[l][r]: the common weights that is common to exercises l~r, inclusive, l <= r
        vector< vector<int> > move(E, vector<int>(E, 0));
        // move[l][r]: the minimum move to finish exercise l~r, inclusive

        for (int l = 0; l < E; l++) {
            vector<int> temp_common = exercises[l];
            common[l][l] = accumulate(temp_common.begin(), temp_common.end(), 0);
            for (int r = l+1; r < E; r++) {
                for (int i = 0; i < W; i++)
                    temp_common[i] = min(temp_common[i], exercises[r][i]);
                common[l][r] = accumulate(temp_common.begin(), temp_common.end(), 0);
                // cout << "l " << l << " r " << r << " " << common[l][r] << endl;
            }
        }

        for (int gap = 1; gap < E; gap++) {
            for (int l = 0; l < E - gap; l++) {
                int r = l + gap;
                int min_move = MAX_INT;
                for (int x = l; x < r; x++) {
                    int curr_move = move[l][x] + move[x+1][r] + 2 * (common[l][x] - common[l][r]) + 2 * (common[x+1][r] - common[l][r]);
                    min_move = min(min_move, curr_move);
                    // cout << "l " << l << " r " << r << " x " << x << " " << curr_move << endl;
                }
                move[l][r] = min_move;
            }
        }

        printf("Case #%d: %d\n", t + 1, move[0][E-1] + 2 * common[0][E-1]);
    }
}
