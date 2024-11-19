class Solution {
public:
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<vector<int>> descendants(numCourses, vector<int>());
        vector<int> status(numCourses, 0); // 0: unvisited, 1: visited, 2: completed
        stack<int> visitedNode;
        // record every course's descendants
        for (pair<int, int> p : prerequisites)
       		descendants[p.first].push_back(p.second);

       	// DFS
       	visitedNode.push(0);
        while (!visitedNode.empty()) {
        	int current = visitedNode.top(), uncheckedDescendants = 0;
        	status[current] = 1;
        	for (int i : descendants[current]) {
        		if (status[i] == 1)
        			return false;
        		if (status[i] == 0) {
        			visitedNode.push(i);
        			uncheckedDescendants ++;
        		}
        	}
        	if (uncheckedDescendants == 0) {
        		status[current] = 2;
        		visitedNode.pop();
        	}
        	if (visitedNode.empty()) {
        		for (int i = 0; i < numCourses; i++) {
        			if (status[i] == 0) {
        				visitedNode.push(i);
        				break;
        			}
        		}
        	}
        }
        return true;
    }
};