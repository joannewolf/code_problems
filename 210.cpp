class Solution {
public:
    vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<vector<int>> ascendants(numCourses, vector<int>());
        vector<bool> checked(numCourses, false);
        vector<int> result;

        for (pair<int, int> p : prerequisites)
        	ascendants[p.first].push_back(p.second);
        while (true) {
        	vector<int> noParentNodes;
        	for (int i = 0; i < ascendants.size(); i++) {
        		if (!checked[i] && ascendants[i].size() == 0) {
        			noParentNodes.push_back(i);
        			checked[i] = true;
        			result.push_back(i);
        		}
        	}
        	if (noParentNodes.empty())
        		break;
        	for (int i : noParentNodes) {
        		for (int j = 0; j < numCourses; j++) {
        			if (!checked[j] && find(ascendants[j].begin(), ascendants[j].end(), i) != ascendants[j].end())
        				ascendants[j].erase(find(ascendants[j].begin(), ascendants[j].end(), i));
        		}
        	}
        }
        for (int i = 0; i < numCourses; i++)
        	if (!ascendants[i].empty())
        		return vector<int>();
        return result;
    }
};