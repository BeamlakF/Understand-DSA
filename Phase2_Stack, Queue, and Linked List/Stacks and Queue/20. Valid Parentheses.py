class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  
        pairs = {')': '(', ']': '[', '}': '{'}  

        for char in s:
            if char in "([{":
                stack.append(char)

            elif char in ")]}":
                if not stack:
                # if stack is empty:
                    return False
                
                top = stack.pop()
                if pairs[char] != top:
                    return False

# at the end, stack must be empty for valid string

        if len(stack)==0:
            return True
        else:
            return False
            
            

            