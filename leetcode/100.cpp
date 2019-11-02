/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// by recursion
class Solution {
public:
	bool isSameTree(TreeNode* p, TreeNode* q) {
		if (p == NULL && q == NULL)
			return true;
		else if (((p == NULL) != (q == NULL)) || (p -> val != q -> val))
			return false;
		else
			return (isSameTree(p -> left, q -> left) & isSameTree(p -> right, q -> right));
	}
};

// by iteration
class Solution {
public:
	bool isSameTree(TreeNode* p, TreeNode* q) {
		stack<TreeNode*> pNodes, qNodes;
		pNodes.push(p);
		qNodes.push(q);

		while (!pNodes.empty() && !qNodes.empty()) {
			TreeNode *pTemp = pNodes.top();
			TreeNode *qTemp = qNodes.top();
			pNodes.pop();
			qNodes.pop();
			if ((pTemp == NULL && qTemp != NULL) || (pTemp != NULL && qTemp == NULL) || (pTemp != NULL && qTemp != NULL && pTemp -> val != qTemp -> val))
				return false;
			else if (pTemp != NULL && qTemp != NULL) {
				pNodes.push(pTemp -> left);
				qNodes.push(qTemp -> left);
				pNodes.push(pTemp -> right);
				qNodes.push(qTemp -> right);
			}
		}
		return true;
	}
};