// Product Triplets
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051066/0000000000051187
// O(N^2)

#include <bits/stdc++.h>
#include <unordered_map>

typedef long long ll;

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N;
        cin >> N;
        unordered_map<ll, ll> num_count;
        for (int i = 0; i < N; i++) {
            ll temp;
            cin >> temp;
            if (num_count.find(temp) == num_count.end())
                num_count[temp] = 1;
            else
                num_count[temp] += 1;
        }
        // for (auto it : num_count) {
        //     cout << it.first << " " << it.second << endl;
        // }

        ll ans = 0;
        if (num_count.find(0) != num_count.end()) { // 0 times anything equals 0
            ll zeros = num_count[0];
            num_count.erase(0);
            ans += zeros * (zeros - 1) * (zeros - 2) / 6; // (0, 0, 0)
            ans += zeros * (zeros - 1) / 2 * (N - zeros); // (0, 0, x)
        }
        if (num_count.find(1) != num_count.end()) { // 1 times anything equals to themselves
            ll ones = num_count[1];
            num_count.erase(1);
            ans += ones * (ones - 1) * (ones - 2) / 6; // (1, 1, 1)
            for (auto it : num_count) {
                if (it.second >= 2) {
                    int x = it.second;
                    ans += ones * x * (x - 1) / 2; // (1, x, x)
                }
            }
        }

        N = num_count.size();
        vector<ll> nums; // Distinct remaining numbers
        for(auto it : num_count) {
            nums.push_back(it.first);
        }
        // for (int n : nums)
        //     cout << n << " ";
        // cout << endl;
        for (int i = 0; i < N; i++) {
            ll x = num_count[nums[i]];
            if (x >= 2 && num_count.find(nums[i] * nums[i]) != num_count.end()) { // (x, x, y)
                ll y = num_count[nums[i] * nums[i]];
                ans += x * (x - 1) / 2 * y;
            }
            for (int j = i + 1; j < N; j++) {
                if (num_count.find(nums[i] * nums[j]) != num_count.end()) { // (x, y, z)
                    ll y = num_count[nums[j]];
                    ll z = num_count[nums[i] * nums[j]];
                    ans += x * y * z;
                }
            }
        }
        printf("Case #%d: %lld\n", t + 1, ans);
    }
}
