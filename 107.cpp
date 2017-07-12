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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> result, leftResult, rightResult;
        int n, ln, rn;

        if (root == NULL)
            return result;
        if (root -> left == NULL && root -> right == NULL) {
            result.insert(result.begin(), vector<int>(1, root -> val));
            return result;
        }

        if (root -> left != NULL)
            leftResult = levelOrderBottom(root -> left);
        if (root -> right != NULL)
            rightResult = levelOrderBottom(root -> right);
        ln = leftResult.size();
        rn = rightResult.size();
        result.insert(result.begin(), vector<int>(1, root -> val));
        vector<vector<int>> temp(max(ln, rn), vector<int>());
        result.insert(result.begin(), temp.begin(), temp.end());
        n = result.size();
        for (int i = 0; i < leftResult.size(); i++)
            result[n - 2 - i].insert(result[n - 2 - i].end(), leftResult[ln - 1 - i].begin(), leftResult[ln - 1 - i].end());
        for (int i = 0; i < rightResult.size(); i++)
            result[n - 2 - i].insert(result[n - 2 - i].end(), rightResult[rn - 1 - i].begin(), rightResult[rn - 1 - i].end());
        
        return result;
    }
};