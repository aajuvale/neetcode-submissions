class Solution:
    def isValid(self, s: str) -> bool:
        
        # how to solve?
        # Create a stack and then pop the top

        stack = []
        Map = {")":"(",
        "]":"[",
        "}":"{"}

        for char in s:
            if char not in Map:
                stack.append(char)
                continue
            if not stack or stack[-1] != Map[char]:
                return False
            stack.pop()
        
        return not stack