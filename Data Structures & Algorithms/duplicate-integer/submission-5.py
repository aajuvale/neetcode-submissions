class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # This solution would work if you had implemented a sorting algorithm before this so that everything would be side by side. 
        # item = 0
        # for item in nums:
        #     try:
        #         if nums[item] == nums[item + 1]:
        #             return True
        #     except IndexError:
        #         return False
        #     item = item + 1
        
        # return False

        #How to solve this one? use a set

        setVer = set()

        for item in nums:
            if item in setVer:
                return True
            setVer.add(item)
           
        
        return False