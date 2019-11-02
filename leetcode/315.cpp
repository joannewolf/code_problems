// O(NlogN), merge sort
class Solution {
private:
    vector<int> nums;
    vector<int> smallerCount;
    int n;

    void mergeSort(vector<int> &index, int start, int end) {
        if (start >= end)
            return;

        int middle = (start + end) / 2;
        mergeSort(index, start, middle);
        mergeSort(index, middle + 1, end);

        vector<int> newIndex(end - start + 1);
        int leftFlag = start, rightFlag = middle + 1, sortedFlag = 0;
        int rightCount = 0;

        while (leftFlag <= middle && rightFlag <= end) {
            if (nums[index[rightFlag]] < nums[index[leftFlag]]) {
                newIndex[sortedFlag] = index[rightFlag];
                rightCount ++;
                rightFlag ++;
            }
            else {
                newIndex[sortedFlag] = index[leftFlag];
                smallerCount[index[leftFlag]] += rightCount;
                leftFlag ++;
            }
            sortedFlag ++;
        }
        while (leftFlag <= middle) {
            newIndex[sortedFlag] = index[leftFlag];
            smallerCount[index[leftFlag]] += rightCount;
            leftFlag ++;
            sortedFlag ++;
        }
        while (rightFlag <= end) {
            newIndex[sortedFlag] = index[rightFlag];
            rightFlag ++;
            sortedFlag ++;
        }


        for (int i = start; i <= end; i++) {
            index[i] = newIndex[i - start];
        }
    }
public:
    vector<int> countSmaller(vector<int>& nums) {
    	this -> nums = nums;
        n = nums.size();
        smallerCount = vector<int> (n, 0);

        vector<int> index(n, 0);
        for (int i = 0; i < n; i++)
            index[i] = i;

        mergeSort(index, 0, n - 1);

        return smallerCount;
    }
};

// O(NlogN), insertion sort
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<int> sortedNums;
        vector<int> smallerCount(n, 0);

        for (int i = n - 1; i >= 0; i--) {
            int l = 0, r = sortedNums.size() - 1;
            while (l <= r) {
                int middle = (l + r) / 2;
                if (sortedNums[middle] < nums[i])
                    l = middle + 1;
                else
                    r = middle - 1;
            }
            smallerCount[i] = l;
            sortedNums.insert(sortedNums.begin() + l, nums[i]);
        }

        return smallerCount;
    }
};