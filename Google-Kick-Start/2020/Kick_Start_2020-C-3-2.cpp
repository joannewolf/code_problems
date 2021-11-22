// Perfect Subarray
// https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003381cb
// O(N * sqrt(N * MAX_A))

#include <iostream>
#include <vector>
#include <utility>
#include <math.h>
#include <algorithm>
#include <set>
#include <unordered_map>

#define ll long long

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N;
        cin >> N;
        vector<ll> nums;
        ll max_num = 0;
        for (int i = 0; i < N; i++) {
            ll num;
            cin >> num;
            if (num > max_num)
                max_num = num;
            nums.push_back(num);
        }

        vector<ll> square;
        for (int i = 0; i <= sqrt(max_num * N); i++)
            square.push_back(i * i);

        ll ans = 0;
        unordered_map<ll, int> prefix_sum; // # prefix_sum[key]: the number of indices i such that sum(A[0...i])=key
        prefix_sum[0] = 1;
        ll current_sum = 0;
        for (int i = 0; i < N; i++) {
            current_sum += nums[i];
            for (int j = 0; j < square.size(); j++) {
                if (prefix_sum.find(current_sum - square[j]) != prefix_sum.end()) {
                    // Because sum of subarray = current_sum A[0...i] - prefix_sum A[0...j]
                    ans += prefix_sum[current_sum - square[j]];
                }
            }
            if (prefix_sum.find(current_sum) != prefix_sum.end())
                prefix_sum[current_sum] += 1;
            else
                prefix_sum[current_sum] = 1;
        }
        printf("Case #%d: %lld\n", t + 1, ans);
    }
}
