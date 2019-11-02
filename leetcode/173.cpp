/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
private:
	stack<TreeNode*> nextNodes;
	void pushAll(TreeNode* node) {
		while (node != NULL) {
			nextNodes.emplace(node);
			node = node -> left;
		}
	}
public:
    BSTIterator(TreeNode *root) {
    	pushAll(root);
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !nextNodes.empty();
    }

    /** @return the next smallest number */
    int next() {
        TreeNode *current = nextNodes.top();
        nextNodes.pop();
        pushAll(current -> right);
        return current -> val;
    }
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */