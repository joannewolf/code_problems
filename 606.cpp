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
    string result;
    void printTree(TreeNode *node) {
        if (node == NULL)
            return;
        result += to_string(node -> val);
        if (node -> left == NULL && node -> right == NULL)
            return;
        result += "(";
        printTree(node -> left);
        result += ")";
        if (node -> right != NULL) {
            result += "(";
            printTree(node -> right);
            result += ")";
        }
    }
public:
    string tree2str(TreeNode* t) {
        printTree(t);
        return result;
    }
};