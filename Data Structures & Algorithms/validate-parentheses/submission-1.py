class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        def Opening(c: str):
            if c in ['(', '{', '[']:
                return True
            return False
        
        def Match(c: str):
            if c == '(':
                return ")"
            if c== "{":
                return "}"
            if c == "[":
                return "]"
            return None


        for i in s:

            if Opening(i):
                stack.append(i)
            else:
                if stack == []:
                    return False
                
                openingType = stack.pop()
                if i != Match(openingType):
                    return False
        
        return True and stack == []


        