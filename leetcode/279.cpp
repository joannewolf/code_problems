// dynamic programming
class Solution {
public:
	int numSquares(int n) {
		vector<int> combinations(n + 1, INT_MAX);
		combinations[0] = 0;
		for (int i = 1; i <= n; i++) {
			for (int j = 1; i - (j * j) >= 0; j++)
				combinations[i] = min(combinations[i], combinations[i - j * j] + 1);
		}
		return combinations.back();
	}
};

// mathematical
// https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
// there are only 4 possible results: 1, 2, 3, 4
class Solution {
private:
	bool isSquare(int n) {
		int root = (int) sqrt(n);
		return (root * root == n);
	}
public:
	int numSquares(int n) {
		if (isSquare(n))
			return 1;

		// result is 4 if and only if n can be written in the form 4^k(8m+7)
		while (n % 4 == 0)
			n >>= 2;
		if (n % 8 == 7)
			return 4;

		// check whether result is 2
		int root = (int) sqrt(n);
		for (int i = 1; i <= root; i++) {
			if (isSquare(n - i * i))
				return 2;
		}

		return 3;
	}
};

// BFS + memorization
class Solution {
public:
	int numSquares(int n) {
		vector<int> countPerfectSquares(n + 1, -1);
		// countPerfectSquares[i]: the least number of perfect square numbers sum to i
		countPerfectSquares[0] = 0;

		queue<int> toBeChecked;
		int count = 0;
		toBeChecked.emplace(0);
		while (!toBeChecked.empty()) {
			count ++;
			int checkSize = toBeChecked.size();
			for (int i = 0; i < checkSize; i++) {
				int temp = toBeChecked.front();
				toBeChecked.pop();

				for (int j = 1; j * j <= n - temp; j++) {
					int current = temp + j * j;
					if (current == n)
						return count;
					else if (countPerfectSquares[current] == -1) {
						countPerfectSquares[current] = count;
						toBeChecked.emplace(current);
					}
				}
			}
		}

		return 0;
	}
};