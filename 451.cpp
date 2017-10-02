#include <map>
#include <utility>
#include <algorithm>
class Solution {
private:
	static bool cmpValue(pair<char, int> a, pair<char, int> b) {
		return (a.second > b.second);
	}
public:
    string frequencySort(string s) {
        map<char, int> counts;
        vector<pair<char, int>> countsVec;
        string result;
        for (char c : s) {
        	if (counts.find(c) == counts.end())
        		counts[c] = 1;
        	else
        		counts[c] ++;
        }
        for (map<char, int>::iterator it = counts.begin(); it != counts.end(); it++)
        	countsVec.push_back(make_pair(it -> first, it -> second));
        sort(countsVec.begin(), countsVec.end(), cmpValue);
        for (pair<char, int> p : countsVec)
        	result += string(p.second, p.first);
        return result;
    }
};