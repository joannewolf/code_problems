// Burger Optimization
// https://codingcompetitions.withgoogle.com/codejamio/round/000000000005102c/0000000000050dd4

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T;
	
	cin >> T;
	for (int i = 0; i < T; i++) {

		// get input for each case
		int K, ans = 0;
		cin >> K;		
		int temp;
		vector<int> opt_dis;
		for (int j = 0; j < K; j++) {
			cin >> temp;
			opt_dis.push_back(temp);
		}
		
		sort(opt_dis.begin(), opt_dis.end());
		for (int j = 0; j < K; j++) {
			ans += (opt_dis[j] - j / 2) * (opt_dis[j] - j / 2);
		}
		
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	
	return 0;
}