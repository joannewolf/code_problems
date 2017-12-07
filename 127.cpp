#include <algorithm>
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        if (wordList.size() == 0 || find(wordList.begin(), wordList.end(), endWord) == wordList.end())
        	return 0;

        wordList.emplace_back(beginWord);
        int n = wordList.size(), str_n = beginWord.length();
        int beginIdx = n - 1, endIdx = find(wordList.begin(), wordList.end(), endWord) - wordList.begin();

        // construct the graph
        vector<vector<int>> transformable(n);
        for (int i = 0; i < n - 1; i ++) {
        	for (int j = i + 1; j < n; j ++) {
        		int diff_count = 0;
        		for (int k = 0; k < str_n; k++) {
        			if (wordList[i][k] != wordList[j][k])
        				diff_count ++;
        			if (diff_count > 1)
        				break;
        		}
        		if (diff_count == 1) {
        			transformable[i].emplace_back(j);
        			transformable[j].emplace_back(i);
        		}
        	}
        }

        // do BFS
        vector<int> distance(n, 0);
        queue<int> toBeChecked;

        toBeChecked.emplace(beginIdx);
        distance[beginIdx] = 1;

        while(!toBeChecked.empty()) {
            int temp = toBeChecked.front();
            toBeChecked.pop();

            for (int i : transformable[temp]) {
                if (distance[i] == 0) {
                    distance[i] = distance[temp] + 1;
                    toBeChecked.emplace(i);
                }
            }
        }
        return distance[endIdx];
    }
};