/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int findSecondMinimumValue(TreeNode* root) {
        queue<TreeNode*> toBeChecked;
        int secondMinimum = INT_MAX;

        if (root != NULL)
        	toBeChecked.emplace(root);
        
        while (!toBeChecked.empty()) {
        	TreeNode *current = toBeChecked.front();
        	toBeChecked.pop();
        	if (current -> left != NULL && current -> right != NULL) {
        		if (current -> left -> val == current -> right -> val) {
        			toBeChecked.emplace(current -> left);
        			toBeChecked.emplace(current -> right);
        		}
        		else if (current -> left -> val < current -> right -> val) {
        			secondMinimum = min(secondMinimum, current -> right -> val);
        			toBeChecked.emplace(current -> left);
        		}
        		else {
        			secondMinimum = min(secondMinimum, current -> left -> val);
        			toBeChecked.emplace(current -> right);
        		}
        	}
        }

        return ((secondMinimum != INT_MAX) ? secondMinimum : -1);
    }
};