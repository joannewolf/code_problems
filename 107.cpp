/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// by BFS, top down
class Solution {
private:
	vector<vector<int>> nodeList;
	void printOrder(int level, TreeNode *node) {
		if (node == NULL)
			return;
		if (nodeList.size() < level)
			nodeList.insert(nodeList.begin(), vector<int>());
		nodeList[nodeList.size() - level].push_back(node -> val);
		if (node -> left != NULL)
			printOrder(level + 1, node -> left);
		if (node -> right != NULL)
			printOrder(level + 1, node -> right);
	}
public:
	vector<vector<int>> levelOrderBottom(TreeNode* root) {
		printOrder(1, root);
		return nodeList;
	}
};

// by BFS, bottom up
class Solution {
public:
	vector<vector<int>> levelOrderBottom(TreeNode* root) {
		if (root == NULL)
			return vector<vector<int>>();
		
		vector<vector<int>> leftResult = levelOrderBottom(root -> left);
		vector<vector<int>> rightResult = levelOrderBottom(root -> right);
		vector<vector<int>> result(max(leftResult.size(), rightResult.size()) + 1);
		int n = result.size(), ln = leftResult.size(), rn = rightResult.size();

		result.back().push_back(root -> val);
		for (int i = 0; i < ln; i++)
			result[n - 2 - i].insert(result[n - 2 - i].end(), leftResult[ln - 1 - i].begin(), leftResult[ln - 1 - i].end());
		for (int i = 0; i < rn; i++)
			result[n - 2 - i].insert(result[n - 2 - i].end(), rightResult[rn - 1 - i].begin(), rightResult[rn - 1 - i].end());
		
		return result;
	}
};

// by DFS
class Solution {
public:
	vector<vector<int>> levelOrderBottom(TreeNode* root) {
		vector<vector<int>> result;
		stack<pair<TreeNode*, int>> nodeStack;

		nodeStack.push(make_pair(root, 0));
		while (!nodeStack.empty()) {
			TreeNode *current = nodeStack.top().first;
			int level = nodeStack.top().second;
			nodeStack.pop();

			if (current != NULL) {
				if (result.size() < level + 1)
					result.insert(result.begin(), vector<int>());
				result[result.size() - 1 - level].push_back(current -> val);
				nodeStack.push(make_pair(current -> right, level + 1));
				nodeStack.push(make_pair(current -> left, level + 1));
			}
		}

		return result;
	}
};