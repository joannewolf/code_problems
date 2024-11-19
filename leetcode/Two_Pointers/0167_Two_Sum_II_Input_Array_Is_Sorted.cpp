class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int front = 0, end = numbers.size() - 1;
        while (front < end) {
            int temp = numbers[front] + numbers[end];
            if (temp < target)
                front ++;
            else if (temp > target)
                end --;
            else {
                vector<int> result;
                result.push_back(front + 1);
                result.push_back(end + 1);
                return result;
            }
        }
    }
};