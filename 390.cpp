class Solution {
public:
    int lastRemaining(int n) {
        int direction = 1; // left: 1, right: -1
        int remaining = n;
        int head = 1;
        int step = 1;
        while (remaining > 1) {
        	if ((direction == 1) || (direction == -1 && remaining % 2 == 1))
        		head += step;
        	step *= 2;
        	direction = -direction;
        	remaining /= 2;
        }
        return head;
    }
};