import math

"""
Stirling’s formula is a mathematical formula used to estimate the value of 𝑛! for large positive integers 𝑛. 
Because factorials grow extremely quickly, direct calculation becomes difficult; this formula provides a high‑accuracy 
estimate using elementary mathematical constants like 𝑒 and π.

"""

class StirlingFormula:
    def __init__(self, n):
        
        if not isinstance(n, (int, float)) or n < 0:
            raise ValueError("n must be a non-negative number.")
        if n == 0:
            print("Note: 0! is exactly 1 by definition.")
            
        self.n = n
        
    def calculate(self):
        first_path = math.sqrt(2 * math.pi * self.n)
        second_path = (self.n / 2.71828) ** self.n
        third_path = first_path * second_path
        return math.ceil(third_path)
    
    #or
    
    def calculate2(self):
        first_path = math.sqrt(2 * math.pi * self.n)
        second_path = self.n ** (self.n + 0.5) * math.exp(-self.n)
       
        return math.ceil(second_path)
    
    def check_diff (self):
        return math.perm(self.n) - self.calculate()


n = 5
n2 = 50
stirling = StirlingFormula(n)
stirling2 = StirlingFormula(n2)
result = stirling.calculate()   
result2 = stirling2.calculate()
print(f"Stirling's approximation for {n}! is: {result}")
print(f"Stirling's approximation for {n2}! is: {result2}")
print(f"Difference for {n}! is: {stirling.check_diff()}")

print(f"Difference for {n2}! is: {stirling2.check_diff()}")
