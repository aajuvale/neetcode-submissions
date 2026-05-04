class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # input: nums array
        # output: consecutive number longest path

        numSet = set(nums)
        count = 0

        for n in nums:
            #check if it is the start of a sequence
            if n - 1 not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                count = max(length, count)
                


        # for index in range(len(nums)):
        #     initialVal = nums[index]
            
        #     # i = 1
        #     if initialVal - 1 in nums:
        #         print("initialVal:")
        #         print(initialVal)
        #         print("initialVal-1:")
        #         print(initialVal-1)
        #         print("count")
        #         count += 1
        #         print(count)
        #     else:
        #         count = 1
           
        #     # if index == 0 and initialVal + 1 not in nums:
        #     #     print("gettin here")
        #     #     count = 1
        
        return count