class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        

        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and temp > stack[-1]:
                stackT = stack.pop()
                stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append(i)
            stack.append(temp) 
        return res
            
                


        