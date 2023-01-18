class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            if (stack[-1] if len(stack) > 0 else "") == self.other(letter):
                stack.pop()
            else:
                stack.append(letter)
        return len(stack) == 0
    
    def other(self, ch: str) -> str:
        return {"{": None, "}": "{", "(": None, ")": "(", "[": None, "]": "["}[ch]
