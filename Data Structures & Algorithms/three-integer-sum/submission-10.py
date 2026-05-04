class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        outList = []
        for i, n in enumerate(nums):
            #because the first number has to be a negative number for any sum to be zero
            if n > 0: 
                break
            if i > 0 and n == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if n + nums[left] + nums[right] > 0:
                    right -= 1
                elif n + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    outList.append([n, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return outList

            
        