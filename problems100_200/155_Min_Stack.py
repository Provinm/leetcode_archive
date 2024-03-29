#coding=utf-8

'''
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

'''

class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """

        self.stack.pop(-1)
        

    def top(self):
        """
        :rtype: int
        """

        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """

        return min(self.stack)

