// O(N^2)
class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		for (int i = 0; i < nums.size(); i++) {
			for (int j = i + 1; j < nums.size(); j++) {
				if (nums[i] + nums[j] == target)
					return vector<int>{i, j};
			}
		}
	}
};

// O(NlogN)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> nums2 (nums);
        sort(nums2.begin(), nums2.end());
        int front = 0, end = nums2.size() - 1;
        while (1) {
        	int temp = nums2[front] + nums2[end];
        	if (temp > target)
        		end --;
        	else if (temp < target)
        		front ++;
        	else {
        		vector<int> result;
        		result.push_back( find(nums.begin(), nums.end(), nums2[front]) - nums.begin() );
        		if (nums2[front] == nums2[end])
        			result.push_back( find(nums.begin() + result[0] + 1, nums.end(), nums2[end]) - nums.begin() );
        		else
        			result.push_back( find(nums.begin() , nums.end(), nums2[end]) - nums.begin() );
        		return result;
        	}
        }
    }
};

// O(N)
class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		unordered_map<int, int> index;

		for (int i = 0; i < nums.size(); i++) {
			if (index.find(target - nums[i]) != index.end())
				return vector<int>{index[target - nums[i]], i};
			else
				index[nums[i]] = i;
		}
	}
};