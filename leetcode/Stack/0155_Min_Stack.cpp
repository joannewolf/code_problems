#include <stack>
class MinStack {
public:
    void push(int x) {
        if (minStack.empty() || x <= minStack.top())
            minStack.push(x);
        Stack.push(x);
    }

    void pop() {
        if (Stack.top() == minStack.top())
            minStack.pop();
        Stack.pop();
    }

    int top() {
        return Stack.top();
    }

    int getMin() {
        return minStack.top();
    }
private:
    stack<int> Stack;
    stack<int> minStack;
};