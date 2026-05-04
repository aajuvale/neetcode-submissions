class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # maxNum = 0
        count = 0
        for val in nums:
            # maxNum = max(maxNum, val)
            if count not in nums:
                return count
            count += 1

        return count            
        