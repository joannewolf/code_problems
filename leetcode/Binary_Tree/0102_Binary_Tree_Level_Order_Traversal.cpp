/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// by BFS, iteration
class Solution {
public:
	vector<vector<int>> levelOrder(TreeNode* root) {
		vector<vector<int>> result;
		queue<pair<TreeNode*, int>> toBeChecked;

		toBeChecked.emplace(make_pair(root, 1));
		while (!toBeChecked.empty()) {
			pair<TreeNode*, int> current = toBeChecked.front();
			toBeChecked.pop();

			if (current.first == NULL)
				continue;
			if (result.size() < current.second)
				result.emplace_back(vector<int>());
			result[current.second - 1].emplace_back(current.first -> val);

			toBeChecked.emplace(make_pair(current.first -> left, current.second + 1));
			toBeChecked.emplace(make_pair(current.first -> right, current.second + 1));
		}
		return result;
	}
};

// by DFS, recursion
class Solution {
private:
	vector<vector<int>> nodeList;
	void printOrder(int level, TreeNode *node) {
		if (node == NULL)
			return;
		if (nodeList.size() < level)
			nodeList.emplace_back(vector<int>());

		nodeList[level - 1].push_back(node -> val);
		printOrder(level + 1, node -> left);
		printOrder(level + 1, node -> right);
	}
public:
	vector<vector<int>> levelOrder(TreeNode* root) {
		printOrder(1, root);
		return nodeList;
	}
};

// by DFS, recursion
class Solution {
public:
	vector<vector<int>> levelOrder(TreeNode* root) {
		if (root == NULL)
			return vector<vector<int>>();

		vector<vector<int>> leftResult = levelOrder(root -> left);
		vector<vector<int>> rightResult = levelOrder(root -> right);
		
		vector<vector<int>> result(max(leftResult.size(), rightResult.size()) + 1);
		result[0].emplace_back(root -> val);
		for (int i = 0; i < leftResult.size(); i++)
			result[i + 1].insert(result[i + 1].end(), leftResult[i].begin(), leftResult[i].end());
		for (int i = 0; i < rightResult.size(); i++)
			result[i + 1].insert(result[i + 1].end(), rightResult[i].begin(), rightResult[i].end());
		return result;
	}
};