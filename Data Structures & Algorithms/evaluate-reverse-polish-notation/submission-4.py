class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            # if t.isdigit():
            #     stack.append(int(t))
            if t == '+':
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif t == '-':
                second = stack.pop()
                first = stack.pop()
                res = first - second
                stack.append(res)
            elif t == '*':
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif t == '/':
                second = stack.pop()
                first = stack.pop()
                res = int(first / second)
                stack.append(res)
            else:
                stack.append(int(t))

        return stack[0]
        