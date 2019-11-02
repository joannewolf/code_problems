// Newton's method
class Solution {
public:
	int mySqrt(int x) {
		long long root = x;
		while (root * root > x) {
			root = (root + x / root) / 2;
		}
		return root;
	}
};

// binary search
class Solution {
public:
	int mySqrt(int x) {
		int l = 0, r = 46340;
		while(l <= r) {
			int mid = (l + r) / 2;
			if (mid * mid == x)
				return mid;
			else if (mid * mid < x)
				l = mid + 1;
			else
				r = mid - 1;
		}
		return r;
	}
};
