/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// If we use in-order traversal to serialize a binary search tree, we can get a list of values in ascending order
// by iteration
class Solution {
public:
	bool isValidBST(TreeNode* root) {
		if (root == NULL)
			return true;
		TreeNode *current = root, *previous = NULL;
		stack<TreeNode*> st;
		while (current != NULL || !st.empty()) {
			while (current != NULL) {
				st.push(current);
				current = current -> left;
			}
			current = st.top();
			st.pop();
			if (previous != NULL && current -> val <= previous -> val)
				return false;
			previous = current;
			current = current -> right;
		}
		return true;
	}
};

// by recursion
class Solution {
private:
	bool isValid(TreeNode* node, long long min_value, long long max_value) {
		if (node == NULL)
			return true;
		if ((long long)(node -> val) <= min_value || (long long)(node -> val) >= max_value)
			return false;
		return (isValid(node -> left, min_value, node -> val) & isValid(node -> right, node -> val, max_value));
	}
public:
	bool isValidBST(TreeNode* root) {
		return isValid(root, LLONG_MIN, LLONG_MAX);
	}
};

// by recursion II
class Solution {
private:
	bool validate(TreeNode* node, TreeNode* &prev) {
		if (node == NULL)
			return true;
		if (!validate(node->left, prev))
			return false;
		if (prev != NULL && prev->val >= node->val)
			return false;
		prev = node;
		return validate(node->right, prev);
	}
public:
	bool isValidBST(TreeNode* root) {
		TreeNode* prev = NULL;
		return validate(root, prev);
	}
};