#include <iostream>
#include <vector>
#include <utility>

using namespace std;

// Solution 1
// vector<vector<int> > isDesirable;
// int dfs(int start, int K) {
// 	if (start >= K)
// 		return 0;
// 	int ans = 0;
// 	for (int i = start + 1; i < K + 1; i++) {
// 		if (isDesirable[start][i])
// 			ans = max(ans, 1 + dfs(i, K));
// 	}
// 	return ans;
// }

int main() {
	int T;
	
	cin >> T;
	for (int t = 0; t < T; t++) {
		// get input for each case
		int K;
		cin >> K;
		vector<int> M(K + 1, 0);
		for (int i = 0; i < K + 1; i++)
			cin >> M[i];

		// Solution 1
		// isDesirable[i][j] means Mi ~ Mj is desirable or not
		// 1: desirable, 0: non-desirable
		// isDesirable = vector<vector<int> >(K + 1, vector<int>(K + 1, 0));
		// for (int i = 0; i < K + 1; i++) {
		// 	bool increase = false, decrease = false;
		// 	for (int j = i + 1; j < K + 1; j++) {
		// 		if (M[j] > M[j - 1])
		// 			increase = true;
		// 		else if (M[j] < M[j - 1])
		// 			decrease = true;
		// 		if (increase && decrease) {
		// 			for (int k = j; k < K + 1; k++)
		// 				isDesirable[i][k] = 1;
		// 			break;
		// 		}
		// 	}
		// }
		// for (int i = 0; i < K + 1; i++) {
		// 	for (int j = 0; j < K + 1; j++)
		// 		cout << isDesirable[i][j] << " ";
		// 	cout << endl;
		// }

		// Solution 2
		// startDesirable[i] = j means Mi ~ Mj start becoming desirable, any Mi ~ Mk, k < j, is not desirable
		// vector<int> startDesirable(K + 1, -1);
		// for (int i = 0; i < K + 1; i++) {
		// 	bool increase = false, decrease = false;
		// 	for (int j = i + 1; j < K + 1; j++) {
		// 		if (M[j] > M[j - 1])
		// 			increase = true;
		// 		else if (M[j] < M[j - 1])
		// 			decrease = true;
		// 		if (increase && decrease) {
		// 			startDesirable[i] = j;
		// 			break;
		// 		}
		// 	}
		// }

		int ans = 0, flag = 0;
		// Solution 1
		// ans = dfs(0, K);
		// Solution 2
		// while (startDesirable[flag] != -1) {
		// 	ans ++;
		// 	flag = startDesirable[flag];
		// }
		// cout << endl;
		// Solution 3
		while (flag < K) {
			bool increase = false, decrease = false;
			for (int i = flag + 1; i < K + 1; i++) {
				if (M[i] > M[i - 1])
					increase = true;
				else if (M[i] < M[i - 1])
					decrease = true;
				if (increase && decrease) {
					ans ++;
					flag = i;
					break;
				}
				if (i == K)
					flag = K + 1;
			}
		}

		cout << "Case #" << t + 1 << ": " << ans - 1 << endl;
	}
	
	return 0;
}