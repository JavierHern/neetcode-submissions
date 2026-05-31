class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {')':'(', '}':'{', ']':'['}
        for l in s:
            if l in hash_map:
                if stack and stack[-1] == hash_map[l]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(l)
        return True if not stack else False
