// https://codingcompetitions.withgoogle.com/codejamio/round/000000000005102c/0000000000050dd5

#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>

using namespace std;

int main() {
	int T;
	
	cin >> T;
	for (int i = 0; i < T; i++) {
		
		// get input for each case
		int L;
		cin >> L;
		long long level, num;
		vector< pair<long long, long long> > employees;
		for (int j = 0; j < L; j++) {
			cin >> num;
			cin >> level;
			employees.push_back(make_pair(level, num));
		}

		sort(employees.begin(), employees.end());

		// top-down
		// long long unmanaged = 0, slot = 0;
		// for (int j = L - 1; j >= 0; j--) {
		// 	unmanaged = unmanaged + max(employees[j].second - slot, (long long)0);
		// 	slot = slot - min(employees[j].second, slot) + employees[j].first * employees[j].second;
		// }
		// long long ans = max(unmanaged, employees.back().first + 1);

		// bottom-up
		long long unmanaged = 0;
		for (int j = 0; j < L; j++) {
			unmanaged = max(unmanaged - employees[j].first * employees[j].second, (long long)0) + employees[j].second;
		}
		long long ans = max(unmanaged, employees.back().first + 1);

		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	
	return 0;
}