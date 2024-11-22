// get O(1), put O(1), use hash map and double linked-list
class Node {
public:
	int key;
	int value;
	Node *left, *right;
	Node (int key, int value) {
		this -> key = key;
		this -> value = value;
		left = NULL;
		right = NULL;
	}
};
class LRUCache {
private:
	int capacity;
	unordered_map<int, Node*> nodes;
	Node *head, *tail;

	void deleteNode(Node *node) {
		node -> left -> right = node -> right;
		node -> right -> left = node -> left;
	}

	void addToHead(Node *node) {
		node -> right = head -> right;
		node -> right -> left = node;
		head -> right = node;
		node -> left = head;
	}

	void printNodes() {
		Node *current = head;
		while (current != NULL) {
			printf("(%d, %d), ", current -> key, current -> value);
			current = current -> right;
		}
		cout << endl;
	}
public:
	LRUCache(int capacity) {
		this -> capacity = capacity;
		head = new Node(0, 0);
		tail = new Node(0, 0);
		head -> right = tail;
		tail -> left = head;
	}
	
	int get(int key) {
		if (nodes.find(key) != nodes.end()) {
			deleteNode(nodes[key]);
			addToHead(nodes[key]);
			return nodes[key] -> value;
		}
		else {
			return -1;
		}
	}
	
	void put(int key, int value) {
		if (nodes.find(key) != nodes.end()) {
			nodes[key] -> value = value;
			deleteNode(nodes[key]);
			addToHead(nodes[key]);
		}
		else if (nodes.size() < capacity){
			Node *newNode = new Node(key, value);
			addToHead(newNode);
			nodes[key] = newNode;
		}
		else {
			nodes.erase(tail -> left -> key);
			deleteNode(tail -> left);
			Node *newNode = new Node(key, value);
			addToHead(newNode);
			nodes[key] = newNode;
		}
	}
};

// get O(N), put O(N)
class LRUCache {
private:
	int capacity;
	map<int, int> nums;
	vector<int> records;
	// always keep the least recently used item in the back
public:
	LRUCache(int capacity) {
		this -> capacity = capacity;
	}
	
	int get(int key) {
		auto it = find(records.begin(), records.end(), key);
		if (it != records.end()) {
			records.erase(it);
			records.insert(records.begin(), key);
			return nums[key];
		}
		else
			return -1;
	}
	
	void put(int key, int value) {
		auto it = find(records.begin(), records.end(), key);
		if (it != records.end()) {
			nums[key] = value;
			records.erase(it);
			records.insert(records.begin(), key);
		}
		else if (records.size() == capacity) {
			nums.erase(records.back());
			records.pop_back();
			nums[key] = value;
			records.insert(records.begin(), key);
		}
		else {
			nums[key] = value;
			records.insert(records.begin(), key);
		}
	}
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */