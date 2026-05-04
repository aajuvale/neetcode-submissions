class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hSet = set()

        for idx, val in enumerate(nums):
            if val in hSet:
                return True
            hSet.add(val)
            
        return False