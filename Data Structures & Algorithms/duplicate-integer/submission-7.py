class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        setVer = set()
        for val in nums:
            setVer.add(val)
        
        return len(setVer) != len(nums)
        