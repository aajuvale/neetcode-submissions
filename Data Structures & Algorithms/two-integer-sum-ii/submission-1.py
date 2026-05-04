class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hashMap = {}

        index = 1
        for num in numbers:
            hashMap[num] = index
            index += 1
         
        for num, index in hashMap.items():
            # print("reachin")
            # print(num)
            # print ÷
            if target - num in hashMap:
                print("stretchin")
                if num < (target - num):
                    return [hashMap[num], hashMap[target - num]]
                elif num > (target - num):
                    return [hashMap[target - num], hashMap[num]]

        # for num in numbers:
        #     if target - num in hashMap:
        #         return [num, hashMap]