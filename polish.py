# The evalRPN method evaluates an arithmetic expression in Reverse Polish Notation (RPN).

# Use a stack to process tokens:
# - For operators (+, -, *, /), pop the required operands from the stack, compute the result, and push it back.
# - For numbers, directly push them onto the stack.
# - Ensure division truncates towards zero using `int(float(b) / a)` for the "/" operator.

# Return the final result, which is the only value remaining in the stack.

# TC: O(n) - Single traversal of the tokens list.
# SC: O(n) - Space for the stack.


from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]