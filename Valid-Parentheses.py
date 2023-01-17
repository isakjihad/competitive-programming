class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToopen ={ ")" : "(","]" : "[","}" : "{" }
        for i in s:
            if i in closeToopen:
                if stack and stack[-1]==closeToopen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)  
        return True if not stack else False
            
