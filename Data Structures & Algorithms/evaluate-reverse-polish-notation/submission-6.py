class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = ['+','-','*','/']
        stackk = [] #store numbers
        res = 1


        for i in tokens:
            if i not in symbols:
                stackk.append(int(i))
            else:
                right = stackk.pop()
                left = stackk.pop()
                if i == '+':
                    res = left + right
                elif i == '-':
                    res = left - right
                elif i == '*':
                    res = left * right
                else:
                    res = int(left / right)
                stackk.append(res)

        return stackk[-1]

