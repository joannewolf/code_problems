class Solution {
public:
    string longestWord(vector<string>& words) {
    	map<string, vector<string>> graph;
        vector<string> starts;

        // construct the graph
        for (int i = 0; i < words.size(); i++) {
            if (words[i].length() == 1)
                starts.emplace_back(words[i]);

            for (int j = i + 1; j < words.size(); j++) {
                if (words[i].length() == words[j].length() + 1 && words[j] == words[i].substr(0, words[j].length())) {
                    if (graph.find(words[j]) == graph.end())
                        graph[words[j]] = vector<string>(1, words[i]);
                    else
                        graph[words[j]].emplace_back(words[i]);
                }
                else if (words[i].length() + 1 == words[j].length() && words[i] == words[j].substr(0, words[i].length())) {
                    if (graph.find(words[i]) == graph.end())
                        graph[words[i]] = vector<string>(1, words[j]);
                    else
                        graph[words[i]].emplace_back(words[j]);
                }
            }
        }
        
        // use BFS to traverse the graph and find the leaves
        string longest = "";
        queue<string> toBeChecked;
        for (int i = 0; i < starts.size(); i++)
            toBeChecked.emplace(starts[i]);

        while (!toBeChecked.empty()) {
            string current = toBeChecked.front();
            toBeChecked.pop();
            if (graph.find(current) == graph.end() && (current.length() > longest.length() || (current.length() == longest.length() && current < longest)))
                longest = current;
            else {
                for (int i = 0; i < graph[current].size(); i++)
                    toBeChecked.emplace(graph[current][i]);
            }
        }

        return longest;
    }
};