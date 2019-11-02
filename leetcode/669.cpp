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
	TreeNode* trimBST(TreeNode* root, int L, int R) {
		TreeNode* newRoot = new TreeNode(0);
		newRoot -> left = root;

		stack<TreeNode*> toBeChecked;
		toBeChecked.emplace(newRoot);

		while (!toBeChecked.empty()) {
			TreeNode *current = toBeChecked.top();
			toBeChecked.pop();

			if (current -> left != NULL) {
				if (current -> left -> val >= L && current -> left -> val <= R)
					toBeChecked.emplace(current -> left);
				else if (current -> left -> val < L) {
					current -> left = current -> left -> right;
					toBeChecked.emplace(current);
				}
				else if (current -> left -> val > R) {
					current -> left = current -> left -> left;
					toBeChecked.emplace(current);
				}
			}
			if (current -> right != NULL) {
				if (current -> right -> val >= L && current -> right -> val <= R)
					toBeChecked.emplace(current -> right);
				else if (current -> right -> val < L) {
					current -> right = current -> right -> right;
					toBeChecked.emplace(current);
				}
				else if (current -> right -> val > R) {
					current -> right = current -> right -> left;
					toBeChecked.emplace(current);
				}
			}
		}
		return (newRoot -> left);
	}
};

// by recursion
class Solution {
public:
	TreeNode* trimBST(TreeNode* root, int L, int R) {
		if (root == NULL)
			return NULL;
		else if (root -> val < L) {
			return trimBST(root -> right, L, R);
		}
		else if (root -> val > R) {
			return trimBST(root -> left, L, R);
		}
		else {
			root -> left = trimBST(root -> left, L, R);
			root -> right = trimBST(root -> right, L, R);
			return root;
		}
	}
};