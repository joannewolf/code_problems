// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int l = 1, r = n;
        while (l < r) {
            int middle = l + (r - l) / 2;
            if (isBadVersion(middle))
                r = middle;
            else
                l = middle + 1;
        }

        return l;
    }
};