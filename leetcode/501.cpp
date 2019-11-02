#include <map>
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
public:
    vector<int> findMode(TreeNode* root) {
        map<int, int> counts;
        stack<TreeNode*> s;
        vector<int> result;
        int maxCount = 0;

        if (root == NULL)
            return result;

        // count numbers of all elements
        s.push(root);
        while (!s.empty()) {
            TreeNode *temp = s.top();
            s.pop();
            if (counts.find(temp -> val) == counts.end())
                counts[temp -> val] = 1;
            else
                counts[temp -> val] ++;
            if (temp -> left != NULL)
                s.push(temp -> left);
            if (temp -> right != NULL)
                s.push(temp -> right);
        }
        for (map<int, int>::iterator it = counts.begin(); it != counts.end(); it++) {
            if (it -> second > maxCount) {
                maxCount = it -> second;
                result.clear();
                result.push_back(it -> first);
            }
            else if (it -> second == maxCount)
                result.push_back(it -> first);
        }
        return result;
    }
};