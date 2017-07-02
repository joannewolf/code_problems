#include <climits>
class Solution {
public:
    bool isPerfectSquare(int num) {
        int l = 0, r = 46340;
        // 46340^2 < INT_MAX, 46341^2 > INT_MAX
        while (l < r) {
        	int middle = (l + r) / 2;
        	printf("%d %d %d\n", l, middle, r);
        	if (middle * middle == num)
        		return true;
        	else if (middle * middle < num)
        		l = middle + 1;
        	else if (middle * middle > num)
        		r = middle - 1;
        }
        return (l * l == num);
    }
};