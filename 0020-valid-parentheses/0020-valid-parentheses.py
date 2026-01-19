from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in pairs:
                # Pop and check if it matches top of stack
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                # Push opening brackets
                stack.append(char)

        # Stack should be empty if perfectly valid
        return len(stack) == 0
