#include <map>
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> result;
        if (nums.size() == 0) {
            result.push_back(vector<int>());
            return result;
        }

        // count all the nums
        map<int, int> counts;
        for (int i : nums) {
            if (counts.find(i) == counts.end())
                counts[i] = 1;
            else
                counts[i] ++;
        }

        // create all subsets
        for (int i = 0; i < pow(2, counts.size()); i++) {
            vector<vector<int>> temp(1, vector<int>());
            int num = i;
            map<int, int>::iterator it = counts.begin();
            while (num != 0 && it != counts.end()) {
                if (num & 1) {
                    int curNum = it -> first, curNumCount = it -> second, flag = temp.size();
                    for (int j = 0; j < temp.size(); j++)
                        temp[j].push_back(curNum);
                    vector<vector<int>> temp2(temp);
                    for (int j = 1; j < curNumCount; j ++) {
                        for (int k = 0; k < temp2.size(); k++)
                            temp2[k].push_back(curNum);
                        temp.insert(temp.end(), temp2.begin(), temp2.end());
                    }
                }
                it ++;
                num >>= 1;
            }
            for (vector<int> v : temp)
                result.push_back(v);
        }

        return result;
    }
};