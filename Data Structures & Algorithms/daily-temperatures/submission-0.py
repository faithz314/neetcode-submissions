class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # count the distance between i and the next warmer temperature
        res = [0] * len(temperatures)
        stack = [] # store (temperature, index) for days that HAVEN'T found a warmer day yet
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]: # while stack not empty and current temp is warmer than the top of the stack
                tPop, iPop = stack.pop()
                res[iPop] = i - iPop
            stack.append((temperatures[i], i))
        return res
