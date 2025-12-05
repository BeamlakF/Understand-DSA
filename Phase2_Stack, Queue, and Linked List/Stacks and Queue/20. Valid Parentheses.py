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
            
#Brute force
class Solution:
    def isValid(self, s: str) -> bool:
        old_string = None

        while old_string != s:
            old_string = s
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
           
        if len(s) == 0:
            return True
        else:
            return False

            