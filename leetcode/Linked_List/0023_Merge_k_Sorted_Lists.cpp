/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// O(NlogK), divide and conquer
// N: total # of nodes, K: # of lists
class Solution {
private:
	ListNode* merge2Lists(ListNode* &list1, ListNode* &list2) {
		ListNode* newHead = new ListNode(0), *current = newHead;
		while (list1 != NULL && list2 != NULL) {
			if (list1 -> val < list2 -> val) {
				current -> next = list1;
				list1 = list1 -> next;
			}
			else {
				current -> next = list2;
				list2 = list2 -> next;
			}
			current = current -> next;
		}
		if (list1 != NULL)
			current -> next = list1;
		else if (list2 != NULL)
			current -> next = list2;
		return (newHead -> next);
	}
public:
	ListNode* mergeKLists(vector<ListNode*>& lists) {
		if (lists.size() == 0)
			return NULL;
		while (lists.size() > 1){
			for (int i = 1; i < lists.size(); i ++) {
				lists[i - 1] = merge2Lists(lists[i], lists[i - 1]);
				lists.erase(lists.begin() + i);
			}
		}
		return lists[0];
	}
};

// O(NlogK), use priority queue
class Solution {
private:
	struct cmp {
		bool operator() (pair<int, ListNode*> a, pair<int, ListNode*> b) {
			return a.first > b.first;
		}
	};
public:
	ListNode* mergeKLists(vector<ListNode*>& lists) {
		ListNode* newHead = new ListNode(0), *current = newHead;
		priority_queue<pair<int, ListNode*>, vector<pair<int, ListNode*>>, cmp> pq;

		for (int i = 0; i < lists.size(); i++) {
			if (lists[i] != NULL)
				pq.push(make_pair(lists[i] -> val, lists[i]));
		}

		while (!pq.empty()) {
			ListNode *temp = pq.top().second;
			pq.pop();
			current -> next = temp;
			current = current -> next;
			if (temp -> next != NULL)
				pq.push(make_pair(temp -> next -> val, temp -> next));
		}
		
		return (newHead -> next);
	}
};

// O(NK), merge one by one
class Solution {
public:
	ListNode* mergeKLists(vector<ListNode*>& lists) {
		ListNode* newHead = new ListNode(0), *current = newHead;
		while (!lists.empty()) {
			int minMalue = INT_MAX, flag = -1;
			for (int i = 0; i < lists.size(); i++) {
				if (lists[i] != NULL && lists[i] -> val < minMalue) {
					minMalue = lists[i] -> val;
					flag = i;
				}
				else if (lists[i] == NULL) {
					lists.erase(lists.begin() + i);
					i--;
				}
			}
			if (flag != -1) {
				current -> next = lists[flag];
				lists[flag] = lists[flag] -> next;
				current = current -> next;
			}
		}
		return (newHead -> next);
	}
};

// O(NlogN), brute-force
class Solution {
public:
	ListNode* mergeKLists(vector<ListNode*>& lists) {
		vector<int> nums;
		for (int i = 0; i < lists.size(); i++) {
			ListNode *current = lists[i];
			while (current != NULL) {
				nums.push_back(current -> val);
				current = current -> next;
			}
		}

		sort(nums.begin(), nums.end());

		ListNode *newHead = new ListNode(0), *current = newHead;
		for (int i = 0; i < nums.size(); i++) {
			current -> next = new ListNode(nums[i]);
			current = current -> next;
		}
		return (newHead -> next);
	}
};