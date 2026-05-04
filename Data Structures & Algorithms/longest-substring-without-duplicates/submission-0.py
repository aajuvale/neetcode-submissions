class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setVer = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in setVer:
                setVer.remove(s[left])
                left += 1
            setVer.add(s[right])
            result = max(result, right - left + 1)
        
        
        return result