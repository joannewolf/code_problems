#include <algorithm>
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
    int getMinimumDifference(TreeNode* root) {
        int difference = INT_MAX;
        stack<TreeNode*> s;
        if (root == NULL || (root -> left == NULL && root -> right == NULL))
            return difference;
        s.push(root);
        while (!s.empty()) {
            TreeNode *temp = s.top();
            s.pop();
            if (temp -> left != NULL) {
                s.push(temp -> left);
                TreeNode *flag = temp -> left -> right;
                while (flag != NULL && flag -> right != NULL)
                    flag = flag -> right;
                int tempDiff = (flag == NULL) ? (temp -> left -> val) : max(flag -> val, temp -> left -> val);
                if ((temp -> val) - tempDiff < difference)
                    difference = (temp -> val) - tempDiff;
            }
            if (temp -> right != NULL) {
                s.push(temp -> right);
                TreeNode *flag = temp -> right -> left;
                while (flag != NULL && flag -> left != NULL)
                    flag = flag -> left;
                int tempDiff = (flag == NULL) ? (temp -> right -> val) : min(flag -> val, temp -> right -> val);
                if (tempDiff - (temp -> val) < difference)
                    difference = tempDiff - (temp -> val);
            }
        }

        return difference;
    }
};