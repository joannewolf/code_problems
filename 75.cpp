class Solution {
public:
    void sortColors(vector<int>& nums) {
        int count0 = 0, count1 = 0, count2 = 0;
        for (int i : nums) {
            switch(i) {
                case 0:
                    count0 ++;
                    break;
                case 1:
                    count1 ++;
                    break;
                case 2:
                    count2 ++;
                    break;
            }
        }
        for (int i = 0; i < count0; i++)
            nums[i] = 0;
        for (int i = count0; i < count0 + count1; i++)
            nums[i] = 1;
        for (int i = count0 + count1; i < count0 + count1 + count2; i++)
            nums[i] = 2;
    }
};