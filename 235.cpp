/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// O(N) time, O(1) space, use BST characteristic
class Solution {
public:
	TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
		if (root == NULL)
			return root;

		TreeNode* current = root;
		int smallerVal = min(p -> val, q -> val), biggerVal = max(p -> val, q -> val);
		while (current != NULL) {
			if (current -> val <= biggerVal && current -> val >= smallerVal)
				return current;
			else if (current -> val < smallerVal)
				current = current -> right;
			else
				current = current -> left;
		}
	}
};

// O(N) time, O(N) space
class Solution {
private:
	vector<TreeNode*> printPath(vector<TreeNode*> path, TreeNode* current, TreeNode* target) {
		if (current == NULL)
			return path;
		path.push_back(current);
		if (current == target) {
			return path;
		}
		if (current -> left != NULL) {
			vector<TreeNode*> leftPath = printPath(path, current -> left, target);
			if (leftPath.back() == target)
				return leftPath;
		}
		if (current -> right != NULL) {
			vector<TreeNode*> rightPath = printPath(path, current -> right, target);
			if (rightPath.back() == target)
				return rightPath;
		}
		return path;
	}
public:
	TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
		if (root == NULL)
			return root;
		vector<TreeNode*> pPath = printPath(vector<TreeNode*>(), root, p);
		vector<TreeNode*> qPath = printPath(vector<TreeNode*>(), root, q);
		for (int i = 0; i < min(pPath.size(), qPath.size()); i++) {
			if (pPath[i] != qPath[i])
				return pPath[i - 1];
		}
		return (pPath.size() < qPath.size()) ? pPath.back() : qPath.back();
	}
};