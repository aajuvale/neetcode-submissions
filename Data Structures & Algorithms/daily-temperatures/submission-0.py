class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # results = []
        # tempCount = 0
        # for i in range(len(temperatures)):
            
        #     if i+1 < len(temperatures):
        #         currTemp = temperatures[i]
        #         if currTemp < temperatures[i + 1]:
        #             tempCount += 1
        #     # if i == len(temperatures) - 1:
        #     print(f"prepop values: {temperatures}")
        #     results.append(tempCount)
        #     temperatures.pop(0)
        #     # results.append(temperatures.pop())
        #     print(f"post-pop values: {temperatures}")
        # return results

        res = [0] * len(temperatures)
        stack = [] # pair with temp, index

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res
