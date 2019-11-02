#include <queue>
class Solution {
private:
	bool isMutatable(string s1, string s2) {
		if (s1.length() != s2.length())
			return false;
		int difference = 0;
		for (int i = 0; i < s1.length(); i++) {
			if (s1[i] != s2[i])
				difference ++;
		}
		return (difference == 1);
	}
public:
    int minMutation(string start, string end, vector<string>& bank) {
        int n = bank.size();
        int target = find(bank.begin(), bank.end(), end) - bank.begin();
        vector<vector<int>> graph(n, vector<int>());

        // construct the graph, nodes are strings in the bank, edge means that two strings can mutate to each other
        for (int i = 0; i < n; i++) {
        	for (int j = i + 1; j < n; j++) {
        		if (isMutatable(bank[i], bank[j])) {
        			graph[i].push_back(j);
        			graph[j].push_back(i);        			
        		}
        	}
        }

        // do BFS to find the minimum path to end
        queue<int> toBeChecked;
        vector<int> steps(n, -1);
        for (int i = 0; i < n; i++) {
        	if (isMutatable(start, bank[i])) {
        		toBeChecked.push(i);
        		steps[i] = 1;
        	}
        }
        while (!toBeChecked.empty()) {
        	int temp = toBeChecked.front();
        	toBeChecked.pop();
        	if (temp == target)
        		return steps[temp];
        	else {
        		for (int i : graph[temp]) {
        			if (steps[i] == -1) {
        				toBeChecked.push(i);
        				steps[i] = steps[temp] + 1;
        			}
        		}
        	}
        }
        return -1;
    }
};