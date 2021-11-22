// Centrists
// https://codingcompetitions.withgoogle.com/codejamio/round/000000000005102c/0000000000050dd6

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	int T;
	
	cin >> T;
	for (int i = 0; i < T; i++) {
		
		// get input for each case
		int len;
		cin >> len;
		vector<string> names;
		for (int j = 0; j < 3; j++) {
			string name;
			cin >> name;
			names.push_back(name);
		}

		vector<bool> canBeMiddle(3, true);
		for (int j = 0; j < len; j++) {
			// all three letters are same
			if (names[0][j] == names[1][j] && names[1][j] == names[2][j])
				continue;
			else if (names[0][j] == names[1][j] && names[1][j] != names[2][j]) {
				canBeMiddle[2] = false;
				char usedChar1 = names[1][j], usedChar2 = names[2][j];
				for (int k = j + 1; k < len; k++) {
					if (names[0][k] != names[1][k]) {
						if (names[0][k] == usedChar1 && names[1][k] == usedChar2) {
							canBeMiddle[0] = false;
						}
						else if (names[0][k] == usedChar2 && names[1][k] == usedChar1) {
							canBeMiddle[1] = false;
						}
						break;
					}
				}
			}
			else if (names[1][j] == names[2][j] && names[2][j] != names[0][j]) {
				canBeMiddle[0] = false;
				char usedChar1 = names[2][j], usedChar2 = names[0][j];
				for (int k = j + 1; k < len; k++) {
					if (names[1][k] != names[2][k]) {
						if (names[1][k] == usedChar1 && names[2][k] == usedChar2) {
							canBeMiddle[1] = false;
						}
						else if (names[1][k] == usedChar2 && names[2][k] == usedChar1) {
							canBeMiddle[2] = false;
						}
						break;
					}
				}
			}
			else if (names[2][j] == names[0][j] && names[0][j] != names[1][j]) {
				canBeMiddle[1] = false;
				char usedChar1 = names[0][j], usedChar2 = names[1][j];
				for (int k = j + 1; k < len; k++) {
					if (names[0][k] != names[2][k]) {
						if (names[0][k] == usedChar1 && names[2][k] == usedChar2) {
							canBeMiddle[0] = false;
						}
						else if (names[0][k] == usedChar2 && names[2][k] == usedChar1) {
							canBeMiddle[2] = false;
						}
						break;
					}
				}
			}
			break;
		}
		
		string ans = "Case #" + to_string(i + 1) + ":";
		for (int j = 0; j < 3; j++)
			ans += (canBeMiddle[j] ? " YES" : " NO");
		cout << ans << endl;
	}
	
	return 0;
}