class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         
        # how to solve?
        # multiply every number that is not i

        hashMap = {}  # {} means dict means dict {} means dict


        index = 0
        for i in nums:
            hashMap[index] = i 
            index += 1

        storeOtherVals = []
        # for i in len(hashMap - 1):
        #     hashMap[i] = 1
        #     storeOtherVals.append(hashMap.get(i))

        secondList = []
        result = 1
        for index, val in hashMap.items():
            i = 1 + index
            hashMap[index] = 1

            # while i != index:
            #     print(hashMap.get(i))
            #     if hashMap.get(i) is not None:
            #         storeOtherVals.append(hashMap.get(i))
            #     if hashMap.get(i) is None:
            #         break
            #     i = index
            
            
            # for index, item in hashMap.items():
            indOne = 0
            while indOne < len(hashMap):
                # print(len(hashMap))
                result *= hashMap[indOne]
                indOne += 1
            

            hashMap[index] = val
            print(hashMap)
            secondList.append(result)
            result = 1
        print(secondList)
        return secondList