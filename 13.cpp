class Solution {
public:
    int romanToInt(string s) {
        vector<int> nums;
        int result = 0, buffer = 0;

      	// turn char to int
        for (int i = 0; i < s.length(); i++) {
        	int num = 0;
        	switch(s[i]) {
        		case 'M':
        			num = 1000;
        			break;
        		case 'D':
        			num = 500;
        			break;
        		case 'C':
        			num = 100;
        			break;
        		case 'L':
        			num = 50;
        			break;
        		case 'X':
        			num = 10;
        			break;
        		case 'V':
        			num = 5;
        			break;
        		case 'I':
        			num = 1;
        			break;
        	}
        	nums.push_back(num);
        }
        
        // deal with Roman numerals rules
        for (int i = 0; i < nums.size() - 1; i++) {
        	if (nums[i] < nums[i + 1])
        		buffer += nums[i];
        	else {
        		result += (nums[i] - buffer);
        		buffer = 0;
        	}
        }
        result += (nums.back() - buffer);

        return result;
    }
};