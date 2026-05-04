class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums: 
            return -1

        L = 0
        R = len(nums) - 1

        while L <= R:
            middle = (L+R) // 2
            if target == nums[middle]:
                return middle
            
            # left sorted portion
            if nums[L] <= nums[middle]:
                if target > nums[middle] or target < nums[L]:
                    L = middle + 1
                else:
                    R = middle - 1
            # right sorted
            else:
                if target < nums[middle] or target > nums[R]:
                    R = middle - 1
                else:
                    L = middle + 1
       
        return -1