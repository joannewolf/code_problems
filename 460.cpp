// get O(1), put O(1), use hash map and double linked-list
class Node {
public:
	int key;
	int value;
	int times;
	Node *left, *right;

	Node (int key, int value) {
		this -> key = key;
		this -> value = value;
		times = 1;
		left = NULL;
		right = NULL;
	}
};
class LFUCache {
private:
	int capacity, size;
	int minTime;
	unordered_map<int, Node*> nodes; // key -> node
	unordered_map<int, Node*> heads, tails; // times -> head, tail

	void deleteNode(Node *node) {
		if (node -> left == heads[node -> times] && node -> right == tails[node -> times]) {
			heads.erase(node -> times);
			tails.erase(node -> times);
		}
		else {
			node -> left -> right = node -> right;
			node -> right -> left = node -> left;
		}
	}

	void addToHead(Node *node) {
		if (heads.find(node -> times) == heads.end())
			createNewHeadAndTail(node -> times);

		node -> right = heads[node -> times] -> right;
		node -> right -> left = node;
		heads[node -> times] -> right = node;
		node -> left = heads[node -> times];
	}

	void createNewHeadAndTail(int times) {
		Node *newHead = new Node(-1, -1);
		Node *newTail = new Node(-1, -1);
		newHead -> right = newTail;
		newTail -> left = newHead;
		heads[times] = newHead;
		tails[times] = newTail;
	}
public:
	LFUCache(int capacity) {
		this -> capacity = capacity;
		size = 0;
		minTime = 0;
	}
	
	int get(int key) {
		if (nodes.find(key) != nodes.end()) {
			deleteNode(nodes[key]);

			if (minTime == nodes[key] -> times && heads.find(nodes[key] -> times) == heads.end())
				minTime ++;

			(nodes[key] -> times) ++;
			addToHead(nodes[key]);
			return (nodes[key] -> value);
		}
		else
			return -1;
	}
	
	void put(int key, int value) {
		if (capacity <= 0)
			return;

		if (nodes.find(key) != nodes.end()) {
			deleteNode(nodes[key]);

			if (minTime == nodes[key] -> times && heads.find(nodes[key] -> times) == heads.end())
				minTime ++;

			(nodes[key] -> times) ++;
			nodes[key] -> value = value;
			addToHead(nodes[key]);
		}
		else if (size == capacity) {
			nodes.erase(tails[minTime] -> left -> key);
			deleteNode(tails[minTime] -> left);

			Node *newNode = new Node(key, value);
			nodes[key] = newNode;
			addToHead(nodes[key]);
			minTime = 1;
		}
		else {
			Node *newNode = new Node(key, value);
			nodes[key] = newNode;
			addToHead(nodes[key]);
			size ++;
			minTime = 1;
		}
	}
};

// get O(N), put O(N) [TLE]
class LFUCache {
private:
	int capacity;
	unordered_map<int, int> nums, times;
	vector<int> records;
	// record [key, times], always keep the least frequently used item in the back
	// if there's tie, keep the least recently used item in latter position
	void pringRecord() {
		for (int i = 0; i < records.size(); i++)
			printf("(%d, %d) ", records[i], times[records[i]]);
		cout << endl;
	}

	void updateRecord(int key) {
		auto it = find(records.begin(), records.end(), key);
		if (it != records.end())
			records.erase(it);

		for (int i = 0; i < records.size(); i++) {
			if (times[key] >= times[records[i]]) {
				records.insert(records.begin() + i, key);
				break;
			}
		}
		if (records.empty() || times[records.back()] > times[key])
			records.emplace_back(key);
	}
public:
	LFUCache(int capacity) {
		this -> capacity = capacity;
	}
	
	int get(int key) {
		if (nums.find(key) != nums.end()) {
			times[key] ++;
			updateRecord(key);
			// pringRecord();
			return nums[key];
		}
		else
			return -1;
	}
	
	void put(int key, int value) {
		if (nums.find(key) != nums.end()) {
			nums[key] = value;
			times[key] ++;
			updateRecord(key);
		}
		else if (records.size() == capacity) {
			if (capacity == 0)
				return;
			nums.erase(records.back());
			times.erase(records.back());
			records.pop_back();

			nums[key] = value;
			times[key] = 1;
			updateRecord(key);
		}
		else {
			nums[key] = value;
			times[key] = 1;
			updateRecord(key);
		}
		// pringRecord();
	}
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */