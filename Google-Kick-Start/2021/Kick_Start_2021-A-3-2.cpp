// Rabbit House
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cb14
// Starting from H = max(grid[i][j]), if its neighbor has height difference greater than 1, make it as H - 1
// Then continue with the second max height grid and so on until all grid are checked
// Instead of using 3-layer for loop, use bucketing to find grids with next height faster
// Each grid can be at most re-added to bucket 4 times because of its 4 neighbors, O(4*R*C) = O(R*C)

#include <iostream>
#include <utility>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int R, C;
        cin >> R;
        cin >> C;

        vector< vector<int> > grid(R, vector<int>(C, 0));
        int max_height = 0;
        for (int i = 0; i < R; i ++) {
            for (int j = 0; j < C; j++) {
                cin >> grid[i][j];
                if (grid[i][j] > max_height) {
                    max_height = grid[i][j];
                }
            }
        }

        vector< vector< pair<int, int> > > bucket(max_height + 1, vector< pair<int, int> >());
        vector< vector<bool> > grid_checked(R, vector<bool>(C, false));
        for (int i = 0; i < R; i ++) {
            for (int j = 0; j < C; j++) {
                bucket[grid[i][j]].push_back(make_pair(i, j));
            }
        }

        // printf("%lu\n", bucket.size());
        // for (int i = 0; i < bucket.size(); i++) {
        //     for (int j = 0; j < bucket[i].size(); j++) {
        //         printf("(%d, %d) ", bucket[i][j].first, bucket[i][j].second);
        //     }
        //     printf("\n");
        // }

        long long result = 0;
        int checked = 0;
        // The lowest possible height is max_height - R - C + 2, imagine the H is on one corner, and the lowest height will be on opposite corner
        for (int h = max_height; h >= max(max_height - R - C + 2, 0); h--) {
            // printf("bucket %d size %lu\n", h, bucket[h].size());
            // for (int j = 0; j < bucket[h].size(); j++) {
            //     printf("(%d, %d) ", bucket[h][j].first, bucket[h][j].second);
            // }
            // printf("\n");
            for (int i = 0; i < bucket[h].size(); i++) {
                int r = bucket[h][i].first;
                int c = bucket[h][i].second;
                if (!grid_checked[r][c]) {
                    // If the neighbor has height difference > 1, make it h - 1
                    if (r != 0 && abs(grid[r][c] - grid[r - 1][c]) > 1) {
                        result += abs((h - 1) - grid[r - 1][c]);
                        grid[r - 1][c] = h - 1;
                        bucket[h - 1].push_back(make_pair(r - 1, c));
                    }
                    if (r != R - 1 && abs(grid[r][c] - grid[r + 1][c]) > 1) {
                        result += abs((h - 1) - grid[r + 1][c]);
                        grid[r + 1][c] = h - 1;
                        bucket[h - 1].push_back(make_pair(r + 1, c));
                    }
                    if (c != 0 && abs(grid[r][c] - grid[r][c - 1]) > 1) {
                        result += abs((h - 1) - grid[r][c - 1]);
                        grid[r][c - 1] = h - 1;
                        bucket[h - 1].push_back(make_pair(r, c - 1));
                    }
                    if (c != C - 1 && abs(grid[r][c] - grid[r][c + 1]) > 1) {
                        result += abs((h - 1) - grid[r][c + 1]);
                        grid[r][c + 1] = h - 1;
                        bucket[h - 1].push_back(make_pair(r, c + 1));
                    }
                    // printf("%d %d -> result %d\n", r, c, result);
                    grid_checked[r][c] = true;
                    checked ++;
                }
            }
            if (checked == R * C)
                break;
        }

        printf("Case #%d: %lld\n", t + 1, result);
    }
}
