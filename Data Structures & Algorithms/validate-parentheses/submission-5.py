class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        valid = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        stack = []
        for c in s: 
            if c in valid and stack:
                val = stack.pop()
                if valid[c] != val:
                    return False 
            else:
                stack.append(c)
        print(stack)
        if len(stack) > 0:
            return False
        return True 


            
        
        