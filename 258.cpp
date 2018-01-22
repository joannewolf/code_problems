// O(1)
// https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
class Solution {
public:
	int addDigits(int num) {
		return (num == 0) ? 0 : ((num % 9 == 0) ? 9 : (num % 9));
		// return (1 + (num - 1) % 9);
	}
};

// by iteration
class Solution {
public:
	int addDigits(int num) {
		while (num >= 10) {
			int temp = 0;
			while (num != 0) {
				temp += (num % 10);
				num /= 10;
			}
			num = temp;
		}
		return num;
	}
};