class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(":")", "[":"]", "{":"}"}

        for ch in s:
            if ch in mapping:
                stack.append(mapping[ch])
            else:
                if not stack or not ch == stack.pop():
                    return False
        return len(stack) == 0