import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # tokens=["1","2","+","3","*","4","-"]
        # [3,3,*]
        # [9,4,-]
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

        stack = []
        for token in tokens:
            if token in ops:
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                val = ops[token](val1,val2)
                stack.append(val)
            else:
                stack.append(token)
        
        return int(stack[0])
