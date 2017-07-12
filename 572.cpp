#include <stack>
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
    bool isSameTree(TreeNode *s, TreeNode *t) {
        if (s == NULL && t == NULL)
            return true;
        if ((s == NULL) != (t == NULL) || s -> val != t -> val)
            return false;
        return (isSameTree(s -> left, t -> left) & isSameTree(s -> right, t -> right));
    }
public:
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if (s == NULL && t == NULL)
            return true;
        if ((s == NULL) != (t == NULL))
            return false;
        stack<TreeNode*> nodeStack;
        nodeStack.push(s);
        while(!nodeStack.empty()) {
            TreeNode *temp = nodeStack.top();
            if (temp -> val == t -> val && isSameTree(temp, t))
                return true;
            nodeStack.pop();
            if (temp -> left != NULL)
                nodeStack.push(temp -> left);
            if (temp -> right != NULL)
                nodeStack.push(temp -> right);
        }
        return false;
    }
};