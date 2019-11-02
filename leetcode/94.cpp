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
	vector<int> inorderTraversal(TreeNode* root) {
		vector<int> result;
		stack<TreeNode*> toBeChecked;
		TreeNode *current = root;
		while (current != NULL || !toBeChecked.empty()) {
			while (current != NULL) {
				toBeChecked.push(current);
				current = current -> left;
			}
			current = toBeChecked.top();
			result.push_back(current -> val);
			toBeChecked.pop();
			current = current -> right;
		}
		return result;
	}
};

// by recursion
class Solution {
public:
	vector<int> inorderTraversal(TreeNode* root) {
		if (root == NULL)
			return vector<int>();
		if (root -> left == NULL && root -> right == NULL)
			return vector<int>(1, root -> val);
		vector<int> leftResult = inorderTraversal(root -> left);
		vector<int> rightResult = inorderTraversal(root -> right);
		leftResult.push_back(root -> val);
		leftResult.insert(leftResult.end(), rightResult.begin(), rightResult.end());
		return leftResult;
	}
};

// Morris Traversal
// https://en.wikipedia.org/wiki/Threaded_binary_tree
class Solution {
public:
	vector<int> inorderTraversal(TreeNode* root) {
		vector<int> result;
		TreeNode *current = root;

		while (current != NULL) {
			if (current -> left == NULL) {
				result.push_back(current -> val);
				current = current -> right;
			}
			else {
				// find the rightmost node in left subtree
				TreeNode *previous = current -> left;
				while (previous -> right != NULL)
					previous = previous -> right;
				previous -> right = current;

				TreeNode *temp = current;
				current = current -> left;
				temp -> left = NULL;
			}
		}

		return result;
	}
};