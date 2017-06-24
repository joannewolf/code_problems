class Solution {
public:
    int mySqrt(int x) {
        // Newton's method
        long long root = x;
        while (root * root > x) {
        	root = (root + x / root) / 2;
        }

        return root;
    }
};