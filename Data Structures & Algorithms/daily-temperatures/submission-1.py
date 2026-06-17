class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # count the distance between i and the next warmer temperature
        res = [0] * len(temperatures)
        stack = [] # store (temperature, index) for days that HAVEN'T found a warmer day yet
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]: # while stack not empty and current temp is warmer than the top of the stack
                tPop, iPop = stack.pop()
                res[iPop] = i - iPop
            stack.append((temperatures[i], i))
        return res

        # example walk through by iteration:
        # [30,38,30,36,35,40,28]
        # stack = [30/0], res= [0, 0, 0, 0, 0, 0, 0]
        # stack = [38/1], res= [1, 0, 0, 0, 0, ,0, 0]
        # stack = [38/1, 30/2], res= [1, 0, 0, 0, 0, 0, 0]
        # stack = [38/1], res= [1, 0, 1, 0, 0, 0, 0, 0]
        # stack = [38/1, 36/3], res= [1, 0, 1, 0, 0, 0, 0, 0]
        # stack = [38/1, 36/3, 35/4], res= [1, 0, 1, 0, 0, 0, 0, 0]
        # stack = [40/5], res= [1, 4, 1, 2, 1, 0, 0] # SINCE 40/5 continuously bigger than all of them
        # stack = [40/5, 28/6], res= [1, 4, 1, 2, 1, 0, 0]

