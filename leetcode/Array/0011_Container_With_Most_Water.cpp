class Solution {
public:
    int maxArea(vector<int>& height) {
        if (height.size() < 2)
            return 0;
        int l = 0, r = height.size() - 1, maxContainer = 0;
        while (l < r) {
            int temp = 0;
            if (height[l] < height[r]) {
                temp = height[l] * (r - l);
                l++;
            }
            else {
                temp = height[r] * (r - l);
                r--;
            }
            if (temp > maxContainer)
                maxContainer = temp;
        }
        return maxContainer;
    }
};