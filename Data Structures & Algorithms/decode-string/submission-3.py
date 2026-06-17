class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substr = ""
                # first while- build the substr with. multiple chars
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                # second while- build the num (perhaps multidigit) of the substr
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                # third step- num * substr appended to the stack
                stack.append(int(num) * substr)
        return "".join(stack)

                    
                
        