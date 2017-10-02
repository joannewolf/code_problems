/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
    	if (head == NULL)
    		return NULL;
        RandomListNode *current = head;
        map<RandomListNode*, RandomListNode*> m;
        
        while (current != NULL) {
        	RandomListNode* newNode = new RandomListNode(current -> label);
        	m[current] = newNode;
        	current = current -> next;
        }

        current = head;
        while (current != NULL) {
        	m[current] -> next = m[current -> next];
        	m[current] -> random = m[current -> random];
        	current = current -> next;
        }

        return m[head];
    }
};