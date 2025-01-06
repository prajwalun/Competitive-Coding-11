# The removeKdigits method removes `k` digits from a number string to form the smallest possible number.

# Use a stack to construct the result:
# - Iterate through digits, removing larger digits from the stack if they make the number larger.
# - Push the current digit onto the stack.
# - After the loop, remove any remaining `k` digits from the end of the stack.

# Convert the stack to a string, strip leading zeros, and return the result, or "0" if empty.

# TC: O(n) - Single traversal of the digits.
# SC: O(n) - Space for the stack.


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
            
        stack = stack[:len(stack) - k]
        res = "".join(stack).lstrip("0")
        return res if res else "0"