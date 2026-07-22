class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in range(len(operations)):
            if operations[i] == "+":
                opSum = res[-1] + res[-2]
                res.append(opSum)
            elif operations[i] == "C":
                res.pop()
            elif operations[i] == "D":
                double = res[-1] * 2
                res.append(double)
            else:
                res.append(int(operations[i]))
        return sum(res)