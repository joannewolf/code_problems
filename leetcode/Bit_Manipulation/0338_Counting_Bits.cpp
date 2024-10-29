class Solution {
public:
    vector<int> countBits(int num) {
    	if (num < 0)
    		return vector<int>();
        vector<int> result, cache;
        int flag = 0;

        result.push_back(0);
        cache.push_back(1);
        for (int i = 1; i <= num; i++) {
        	if (flag < cache.size()) {
        		result.push_back(cache[flag]);
        		flag ++;
        	}
        	else {
        		vector<int> temp(cache);
        		for (int i = 0; i < temp.size(); i++)
        			temp[i] ++;
        		cache.insert(cache.end(), temp.begin(), temp.end());
        		result.push_back(cache[0]);
        		flag = 1;
        	}
        }

        return result;
    }
};