// use graph + BFS
class Solution {
public:
	string longestWord(vector<string>& words) {
		vector<vector<int>> graph(words.size());
		queue<int> toBeChecked;

		// construct the graph
		for (int i = 0; i < words.size(); i++) {
			if (words[i].length() == 1)
				toBeChecked.emplace(i);

			for (int j = i + 1; j < words.size(); j++) {
				if (words[i].length() == words[j].length() + 1 && words[j] == words[i].substr(0, words[j].length())) {
					graph[j].emplace_back(i);
				}
				else if (words[i].length() + 1 == words[j].length() && words[i] == words[j].substr(0, words[i].length())) {
					graph[i].emplace_back(j);
				}
			}
		}
		
		// use BFS to traverse the graph and find the leaves
		string longest = "";
		while (!toBeChecked.empty()) {
			int current = toBeChecked.front();
			toBeChecked.pop();
			if (graph[current].empty() && (words[current].length() > longest.length() || (words[current].length() == longest.length() && words[current] < longest)))
				longest = words[current];
			else {
				for (int i = 0; i < graph[current].size(); i++)
					toBeChecked.emplace(graph[current][i]);
			}
		}

		return longest;
	}
};

// use buckets
class Solution {
public:
	string longestWord(vector<string>& words) {
		int maxWordLength = 30;
		vector<vector<string>> dictionary(maxWordLength + 2);
		dictionary[0].emplace_back("");

		for (string word : words) {
			dictionary[word.length()].emplace_back(word);
		}

		for (int i = 1; i <= maxWordLength + 1; i++) {
			for (int j = 0; j < dictionary[i].size(); j++) {
				if (find(dictionary[i - 1].begin(), dictionary[i - 1].end(), dictionary[i][j].substr(0, i - 1)) == dictionary[i - 1].end()) {
					dictionary[i].erase(dictionary[i].begin() + j);
					j--;
				}
			}
			if (dictionary[i].empty()) {
				sort(dictionary[i - 1].begin(), dictionary[i - 1].end());
				return dictionary[i - 1][0];
			}
		}
		return "";
	}
};

// trie + DFS
class TrieNode {
public:
	char val;
	vector<TrieNode*> children;
	TrieNode (char val) {
		this -> val = val;
		children = vector<TrieNode*>(0);
	}
};
class Solution {
private:
	TrieNode *root;
	string dfs(TrieNode *root) {
		string longest = "";
		for (TrieNode *child : root -> children) {
			string temp = dfs(child);
			if (temp.length() > longest.length() || (temp.length() == longest.length() && temp < longest))
				longest = temp;
		}
		return (root -> val + longest);
	}
public:
	static bool cmpWords(string word1, string word2) {
		return (word1.length() != word2.length()) ? (word1.length() < word2.length()) : (word1 < word2);
	}
	string longestWord(vector<string>& words) {
		// construct trie
		root = new TrieNode(' ');
		sort(words.begin(), words.end(), cmpWords);
		for (string word : words) {
			bool validWord = true;
			TrieNode *current = root;
			for (int i = 0; i < word.size() - 1; i++) {
				bool valid = false;
				for (TrieNode *child : current -> children) {
					if (child -> val == word[i]) {
						current = child;
						valid = true;
						break;
					}
				}
				if (!valid) {
					validWord = false;
					break;
				}
			}
			if (validWord)
				current -> children.emplace_back(new TrieNode(word.back()));
		}

		// DFS
		string result = dfs(root);
		result.erase(result.begin());
		return result;
	}
};

// brute-force
class Solution {
public:
	string longestWord(vector<string>& words) {
		string longest = "";
		set<string> wordSet(words.begin(), words.end());
		for (string word : words) {
			if (word.length() > longest.length() || (word.length() == longest.length() && word < longest)) {
				bool valid = true;
				for (int i = word.length() - 1; i >= 1; i--) {
					if (wordSet.find(word.substr(0, i)) == wordSet.end()) {
						valid = false;
						break;
					}
				}
				if (valid)
					longest = word;
			}
		}

		return longest;
	}
};