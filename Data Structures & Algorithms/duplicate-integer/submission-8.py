class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashNums = {}
        count = 1
        for val in nums:
            if val in hashNums:
                return True
            hashNums[val] = count
        return False
       