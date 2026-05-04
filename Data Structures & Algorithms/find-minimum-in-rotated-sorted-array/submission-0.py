class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        currMin = float('inf')

        while l <= r:
            mid = l + (r - l) // 2
            currMin = min(currMin, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
            
        return min(currMin, nums[l])
        
        # return -1