#include <stack>
class MyQueue {
private:
	stack<int> myStack;
public:
    /** Initialize your data structure here. */
    MyQueue() {
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        stack<int> temp;
        while (!myStack.empty()) {
        	temp.push(myStack.top());
        	myStack.pop();
        }
        myStack.push(x);
        while (!temp.empty()) {
        	myStack.push(temp.top());
        	temp.pop();
        }
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        int result = myStack.top();
        myStack.pop();
        return result;
    }
    
    /** Get the front element. */
    int peek() {
        return myStack.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return myStack.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * bool param_4 = obj.empty();
 */