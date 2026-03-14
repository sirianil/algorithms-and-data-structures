class Solution:
    def isValid(self, s: str) -> bool:
        OPEN_BRACES = ["[", "{", "("]
        CLOSE_BRACES = ["}",  "]", ")"]
        OPEN_AND_CLOSE_MATCH = {
            "}": "{",
            ")":"(",
            "]":"["
        }        
        stack = []
        for i in range(len(s)):
            if s[i] in OPEN_BRACES:
                stack.append(s[i])
            elif s[i] in CLOSE_BRACES:
                if len(stack) == 0:
                     return False    
                popped = stack.pop()
                if OPEN_AND_CLOSE_MATCH.get(s[i]) != popped:
                    return False
        if len(stack) != 0:
            return False
        return True
    
if __name__ == "__main__":
    s = Solution()
    testCases = [
        "[{()}]",
        "()",
        "{()}[]",
        "{",
        "{})(][]"
    ]
    for t in testCases:
        print(s.isValid(t))
                    