class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int diff = 0;
        vector<int> result(2, 0);
        // first pass: XOR all the nums and find out the XOR result of the two answers
        for (int i : nums)
        	diff ^= i;
        
        // second pass: since the diff must have bits that are different in the two answers, find one of those bits
        diff &= -diff;
        // divide all the nums in 2 groups: which has that bit 1 and which has that bit 0, XOR each group to get the answer
        for (int i : nums) {
        	if (i & diff)
        		result[0] ^= i;
        	else
        		result[1] ^= i;
        }
        return result;
    }
};