/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// by iteration
class Solution {
public:
	TreeNode* invertTree(TreeNode* root) {
		stack<TreeNode*> s;
		if (root != NULL)
			s.push(root);
		while (!s.empty()) {
			TreeNode *temp = s.top() -> left;
			s.top() -> left = s.top() -> right;
			s.top() -> right = temp;
			temp = s.top();
			s.pop();
			if (temp -> left != NULL)
				s.push(temp -> left);
			if (temp -> right != NULL)
				s.push(temp -> right);
		}

		return root;
	}
};

// by recursion
class Solution {
public:
	TreeNode* invertTree(TreeNode* root) {
		if (root == NULL)
			return root;
		TreeNode *temp = root -> left;
		root -> left = root -> right;
		root -> right = temp;
		
		invertTree(root -> left);
		invertTree(root -> right);
		return root;
	}
};