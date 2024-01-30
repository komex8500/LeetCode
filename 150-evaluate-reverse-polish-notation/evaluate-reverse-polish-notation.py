class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in range(len(tokens)):
            string = tokens[i]
            if string.isdigit() or (string[0] == "-" and string[1:].isdigit()):
                s.append(int(tokens[i]))
            else:
                n2 = s.pop()
                n1 = s.pop()
                if tokens[i] == "+":
                    s.append(n1+n2)
                elif tokens[i] == "-":
                    s.append(n1-n2)
                elif tokens[i] == "*":
                    s.append(n1*n2)
                elif tokens[i] == "/":
                    s.append(int(n1/n2))
        return s.pop()
