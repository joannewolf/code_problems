#include <iostream>

using namespace std;

double state[110][110][110];
int N;
/*
	use DP
	state (K3, K2, K1, K0): # Three-Known, Two-Known, One-Known, or Zero-Known trios
	initial state: (0, 0, 0, N)
	target state: (0, 0, 0, 0)

	f(state): how many round it would take on average to finish the game from this state
	f(K3, K2, K1, K0) = 1 + f(K3 - 1, K2, K1, K0) -> we can remove K3
*/
double dp(int K2, int K1, int K0) {
	if (K2 == 0 && K1 == 0 && K0 == 0) // All trios are three-known
		return 0;
	if (state[K2][K1][K0] > 0) // This status is calculated
		return state[K2][K1][K0];

	int remaining = K2 + 2 * K1 + 3 * K0;
	double ans = 1;

	// two-known
	if (K2 > 0)
		ans += (double)K2 / remaining * dp(K2 - 1, K1, K0);
	// one-known -> two-known, add one more step to clear the three-known
	if (K1 > 0 && K2 > 0)
		ans += (double)(K1 * 2) / remaining * K2 / (remaining - 1) * (dp(K2, K1 - 1, K0) + 1);
	// one-known -> different one-known
	if (K1 > 1)
		ans += (double)(K1 * 2) / remaining * (K1 * 2 - 2) / (remaining - 1) * dp(K2 + 2, K1 - 2, K0);
	// one-known -> same one-known
	if (K1 > 0)
		ans += (double)K1 * 2 / remaining * 1 / (remaining - 1) * dp(K2, K1 - 1, K0);
	// one-known -> zero-known
	if (K1 > 0 && K0 > 0)
		ans += (double)(K1 * 2) / remaining * (K0 * 3) / (remaining - 1) * dp(K2 + 1, K1, K0 - 1);
	// zero-known -> same zero-known -> same zero-known
	if (K0 > 0)
		ans += (double)K0 * 3 / remaining * 2 / (remaining - 1) * 1 / (remaining - 2) * dp(K2, K1, K0 - 1);
	// zero-known -> same zero-known -> two-known, add one more step to clear the three-known
	if (K0 > 0 && K2 > 0)
		ans += (double)K0 * 3 / remaining * 2 / (remaining - 1) * K2 / (remaining - 2) * (dp(K2, K1, K0 - 1) + 1);
	// zero-known -> same zero-known -> one-known
	if (K0 > 0 && K1 > 0)
		ans += (double)K0 * 3 / remaining * 2 / (remaining - 1) * (K1 * 2) / (remaining - 2) * dp(K2 + 2, K1 - 1, K0 - 1);
	// zero-known -> same zero-known -> different zero-known
	if (K0 > 1)
		ans += (double)K0 * 3 / remaining * 2 / (remaining - 1) * (K0 * 3 - 3) / (remaining - 2) * dp(K2 + 1, K1 + 1, K0 - 2);
	// zero-known -> two-known, add one more step to clear the three-known
	if (K0 > 0 && K2 > 0)
		ans += (double)(K0 * 3) / remaining * K2 / (remaining - 1) * (dp(K2 - 1, K1 + 1, K0 - 1) + 1);
	// zero-known -> one-known
	if (K0 > 0 && K1 > 0)
		ans += (double)(K0 * 3) / remaining * (K1 * 2) / (remaining - 1) * dp(K2 + 1, K1, K0 - 1);
	// zero-known -> different zero-known
	if (K0 > 1)
		ans += (double)(K0 * 3) / remaining * (K0 * 3 - 3) / (remaining - 1) * dp(K2, K1 + 2, K0 - 2);

	state[K2][K1][K0] = ans;
	return ans;
}

int main() {
	int T;
	
	cin >> T;
	for (int t = 0; t < T; t++) {
		// get input for each case
		cin >> N;

		for (int i = 0; i < 110; i++) {
			for (int j = 0; j < 110; j++) {
				for (int k = 0; k < 110; k++) {
					state[i][j][k] = -1;
				}
			}
		}
		double ans = dp(0, 0, N);
		cout << "Case #" + to_string(t + 1) + ": " + to_string(ans) << endl;
	}
	
	return 0;
}