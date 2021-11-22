// Grid Escape
// https://codingcompetitions.withgoogle.com/codejamio/round/0000000000050fc5/0000000000054e9c

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	int T;
	
	cin >> T;
	for (int t = 0; t < T; t++) {
		// get input for each case
		int R, C, K;
		cin >> R;
		cin >> C;
		cin >> K;
		
		if (K > R * C || R <= 0 || C <= 0 || K == R * C - 1)
			cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
		else {
			cout << "Case #" << t + 1 << ": POSSIBLE" << endl;
			vector<string> solution(R, string(C, 'X'));
			// build a snake path to make every room escapable
			for (int i = 0; i < R; i++) {
				if (i % 2 == 0) {
					solution[i] = string(C, 'E');
					solution[i].back() = 'S';
				}
				else {
					solution[i] = string(C, 'W');
					solution[i][0] = 'S';
				}
			}
			// block the last Kth room to make exact K room escapable
			int flagR = R - 1, flagC = (R % 2 == 0) ? 0 : C - 1, directionC = (R % 2 == 0) ? 1 : -1;
			for (int i = 0; i < K; i++) {
				if ((directionC == -1 && flagC != 0) || (directionC == 1 && flagC != C - 1)) {
					flagC += directionC;
				}
				else {
					flagR --;
					directionC = -directionC;
				}
			}
			if (K != R * C) {
				if (solution[flagR][flagC] == 'S' && C != 1)
					solution[flagR][flagC] = (flagC == 0) ? 'E' : 'W';
				else if (flagC == 0 || flagC == C - 1)
					solution[flagR][flagC] = 'N';
				else if (solution[flagR][flagC] == 'E')
					solution[flagR][flagC] = 'W';
				else if (solution[flagR][flagC] == 'W')
					solution[flagR][flagC] = 'E';
			}
			// print out solution
			for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++)
					cout << solution[i][j];
				cout << endl;
			}
		}
	}
	
	return 0;
}