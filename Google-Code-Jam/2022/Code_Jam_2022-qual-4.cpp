// Chain Reactions
// https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45ef7
// Convert the problem to tree with root as abyss, if there's only one branch then just take the max node value
// If facing multiple branches, we need to choose one as main chain and stop others at the common ancestor
// It's always better to choose the branch with min value in main chain, so we get the value of all other larger branch values

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

vector< vector<int> > children;
vector<ll> fun;
vector<int> trigger;

// Return tuple (max fun in main branch, sum of fun value of all side branches)
pair<ll, ll> solve(int root) {
    int now = root, next;
    ll curr_max = fun[now];
    while (children[now].size() == 1) {
        next = children[now][0];
        curr_max = max(curr_max, fun[next]);
        now = next;
    }

    if (children[now].size() == 0)
        return make_pair(curr_max, 0);
    else {
        vector<ll> main_fun, side_fun;
        for (int i = 0; i < children[now].size(); i++) {
            pair<ll, ll> next_res = solve(children[now][i]);
            main_fun.push_back(next_res.first);
            side_fun.push_back(next_res.second);
        }
        ll final_main = max(curr_max, *min_element(main_fun.begin(), main_fun.end()));
        ll final_side = accumulate(main_fun.begin(), main_fun.end(), (ll)0)
            - *min_element(main_fun.begin(), main_fun.end())
            + accumulate(side_fun.begin(), side_fun.end(), (ll)0);
        return make_pair(final_main, final_side);
    }
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N;
        cin >> N;
        fun.clear();
        fun.push_back(0);
        trigger.clear();
        children.clear();
        for (int i = 0; i < N; i++) {
            ll temp;
            cin >> temp;
            fun.push_back(temp);
        }
        for (int i = 0; i < N; i++) {
            int temp;
            cin >> temp;
            trigger.push_back(temp);
        }
        for (int i = 0; i <= N; i++) {
            vector<int> temp;
            children.push_back(temp);
        }
        for (int i = 0; i < N; i++) {
            children[trigger[i]].push_back(i+1);
        }

        pair<ll, ll> ans = solve(0);
        printf("Case #%d: %lld\n", t + 1, ans.first + ans.second);
    }
}
