/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */

// BFS
class Solution {
public:
	UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
		if (node == NULL)
			return NULL;

		map<UndirectedGraphNode*, UndirectedGraphNode*> newNodes;
		queue<UndirectedGraphNode*> toBeChecked;

		// clone all nodes
		toBeChecked.emplace(node);
		newNodes[node] = new UndirectedGraphNode(node -> label);
		while (!toBeChecked.empty()) {
			UndirectedGraphNode *currentNode = toBeChecked.front();
			toBeChecked.pop();

			for (UndirectedGraphNode *neighbor : currentNode -> neighbors) {
				if (newNodes.find(neighbor) == newNodes.end()) {
					UndirectedGraphNode *newNeighbor = new UndirectedGraphNode(neighbor -> label);
					newNodes[neighbor] = newNeighbor;
					toBeChecked.emplace(neighbor);
				}
				(newNodes[currentNode] -> neighbors).emplace_back(newNodes[neighbor]);
			}
		}

		return newNodes[node];
	}
};

// DFS, by recursion
class Solution {
private:
	map<UndirectedGraphNode*, UndirectedGraphNode*> newNodes;
public:
	UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
		if (node == NULL)
			return NULL;
		else if (newNodes.find(node) != newNodes.end())
			return newNodes[node];
		else {
			newNodes[node] = new UndirectedGraphNode(node -> label);
			for (UndirectedGraphNode *neighbor : node -> neighbors)
				(newNodes[node] -> neighbors).emplace_back(cloneGraph(neighbor));
			return newNodes[node]
		}
	}
};

// DFS, by iteration
class Solution {
public:
	UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
		if (node == NULL)
			return NULL;

		map<UndirectedGraphNode*, UndirectedGraphNode*> newNodes;
		stack<UndirectedGraphNode*> toBeChecked;

		newNodes[node] = new UndirectedGraphNode(node -> label);
		toBeChecked.emplace(node);
		while (!toBeChecked.empty()) {
			UndirectedGraphNode *currentNode = toBeChecked.top();
			toBeChecked.pop();

			for (UndirectedGraphNode *neighbor : currentNode -> neighbors) {
				if (newNodes.find(neighbor) == newNodes.end()) {
					newNodes[neighbor] = new UndirectedGraphNode(neighbor -> label);
					toBeChecked.emplace(neighbor);
				}
				(newNodes[currentNode] -> neighbors).emplace_back(newNodes[neighbor]);
			}
		}

		return newNodes[node];
	}
};