import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length: float, width: float = None) -> float:
        if width is None:
            res = (math.pi * math.pow(length, 2))
            return round(res, 2)
        return length * width 
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
