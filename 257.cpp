#include <string>
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
private:
    vector<string> printBSTPaths(TreeNode *node) {
        vector<string> result;
        if (node == NULL)
            return result;
        if (node -> left == NULL && node -> right == NULL) {
            result.push_back("->" + to_string(node -> val));
            return result;
        }
        vector<string> leftResult = printBSTPaths(node -> left), rightResult = printBSTPaths(node -> right);
        for (int i = 0; i < leftResult.size(); i++)
            result.push_back("->" + to_string(node -> val) + leftResult[i]);
        for (int i = 0; i < rightResult.size(); i++)
            result.push_back("->" + to_string(node -> val) + rightResult[i]);
        return result;
    }
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> result;
        if (root == NULL)
            return result;
        if (root -> left == NULL && root -> right == NULL) {
            result.push_back(to_string(root -> val));
            return result;
        }
        vector<string> leftResult = printBSTPaths(root -> left), rightResult = printBSTPaths(root -> right);
        for (int i = 0; i < leftResult.size(); i++)
            result.push_back(to_string(root -> val) + leftResult[i]);
        for (int i = 0; i < rightResult.size(); i++)
            result.push_back(to_string(root -> val) + rightResult[i]);

        return result;
    }
};