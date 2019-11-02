#include <queue>
class MyStack {
private:
    queue<int> myQueue;

public:
    /** Initialize your data structure here. */
    MyStack() {
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        myQueue.push(x);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        queue<int> temp;
        while (myQueue.size() > 1) {
            temp.push(myQueue.front());
            myQueue.pop();
        }
        int result = myQueue.front();
        myQueue = temp;
        return result;
    }
    
    /** Get the top element. */
    int top() {
        return myQueue.back();
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return myQueue.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * bool param_4 = obj.empty();
 */