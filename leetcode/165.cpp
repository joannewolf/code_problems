#include <algorithm>
class Solution {
public:
    int compareVersion(string version1, string version2) {
        vector<int> ver1, ver2;
        string temp;
        for (char c : version1) {
        	if (c != '.')
        		temp.push_back(c);
        	else {
        		ver1.push_back((!temp.empty()) ? stoi(temp) : -1);
        		temp.clear();
        	}
        }
        ver1.push_back((!temp.empty()) ? stoi(temp) : -1);
        temp.clear();
        while (!ver1.empty() && ver1.back() == 0)
        	ver1.pop_back();

        for (char c : version2) {
        	if (c != '.')
        		temp.push_back(c);
        	else {
        		ver2.push_back((!temp.empty()) ? stoi(temp) : -1);
        		temp.clear();
        	}
        }
		ver2.push_back((!temp.empty()) ? stoi(temp) : -1);
        temp.clear();
		while (!ver2.empty() && ver2.back() == 0)
        	ver2.pop_back();

        for (int i = 0; i < min(ver1.size(), ver2.size()); i++) {
        	if (ver1[i] != ver2[i])
        		return (ver1[i] > ver2[i]) ? 1 : -1;
        }
        if (ver1.size() == ver2.size())
        	return 0;
        else
        	return (ver1.size() > ver2.size()) ? 1 : -1;
    }
};