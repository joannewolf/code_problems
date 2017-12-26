// O(N), Dynamic Programming
class Solution {
public:
	int climbStairs(int n) {
		vector<int> steps (n + 1, 0);
		steps[1] = 1; // (1)
		steps[2] = 2; // (1,1) or (2)
		for (int i = 3; i <= n; i++)
			steps[i] = steps[i - 1] + steps[i - 2];
		return steps[n];
	}
};

// O(N), Fibonacci Number
class Solution {
public:
	int climbStairs(int n) {
		if (n == 1)
			return 1;
		int first = 1, second = 2;
		for (int i = 3; i <= n; i++) {
			int third = first + second;
			first = second;
			second = third;
		}
		return second;
	}
};

// O(N), recursion with memo
class Solution {
private:
	vector<int> memo;
	int climbStairs(int i, int n) {
		if (i > n)
			return 0;
		else if (i == n)
			return 1;
		else if (memo[i] != 0)
			return memo[i];
		else {
			memo[i] = climbStairs(i + 1, n) + climbStairs(i + 2, n);
			return memo[i];
		}
	}
public:
	int climbStairs(int n) {
		memo = vector<int>(n + 1, 0);
		return climbStairs(0, n);
	}
};