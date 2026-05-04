class Solution:
    def isValid(self, s: str) -> bool:
        
        # how to solve?
        # Create a stack and then pop the top

        hashMap = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack = []
        
        for val in s:
            if val not in hashMap:
                stack.append(val)
                continue
            if not stack or stack[-1] != hashMap[val]:
                return False
            stack.pop()
            # print(stack)
        
        return not stack