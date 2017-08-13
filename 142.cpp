/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (head == NULL || head -> next == NULL || head -> next -> next == NULL)
            return NULL;
        ListNode *walker = head -> next, *runner = head -> next -> next;

        // check if there's a cycle
        /*
        walker walk 1 step at a time, runner run 2 steps at a time
        if there is a cycle, they will meet eventually
        */
        while (walker != runner) {
        	if (walker == NULL || runner == NULL || runner -> next = NULL)
        		return NULL;
            walker = walker -> next;
            runner = runner -> next -> next;
        }

        // if there's a cycle, find the cycle's head
        /*
        x = distance outside the cycle
        y = distance from cycle start to walker-runner meet point
        z = distance from walker-runner meet point to cycle start
        <walker> 2 * [x + n(y + z) + y] = x + m(y + z) + y <runner>
        -> x = (m - 2n)(y + z) - y -> x = (m - 2n - 1)(y + z) + z
        if walker start from head and runner start fomr meet point at same speed, they will meet at cycle start!!!
        */
        walker = head;
        while (walker != runner) {
        	walker = walker -> next;
        	runner = runner -> next;
        }
        return walker;
    }
};