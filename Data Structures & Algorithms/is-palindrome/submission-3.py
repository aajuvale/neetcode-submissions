class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # how to solve
        # use two pointer solution

        def removeNonAlpha(s) -> str:
            retStr = ""
            for val in s:
                if val.isalnum():
                    retStr += val
        
            return retStr.lower()
        
        
        

        s = removeNonAlpha(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            if s[left] != s[right]: 
                return False
            
            
        
        return True