class Solution {
public:
    int hammingDistance(int x, int y) {
        int difference = x ^ y, distance = 0;
        while (difference != 0) {
            distance += (difference & 1);
            difference >>= 1;
        }
        return distance;
    }
};