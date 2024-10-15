#include <set>
#include <queue>
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
    bool findTarget(TreeNode* root, int k) {
        if (root == NULL || (root -> left == NULL && root -> right == NULL))
        	return false;
        // store all nodes in an array, 
        set<int> s;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
        	TreeNode *node = q.front();
        	q.pop();
        	if (s.find(k - (node -> val)) != s.end())
        		return true;
        	s.insert(node -> val);
        	if (node -> left != NULL)
        		q.push(node -> left);
        	if (node -> right != NULL)
        		q.push(node -> right);
        }
        return false;
    }
};