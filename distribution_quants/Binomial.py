import math
import matplotlib.pyplot as plt

class BinomialDistribution:
    """
    A from-scratch implementation of the Binomial Distribution.
    Parameters:
    - n (int): Number of independent trials.
    - p (float): Probability of success in each trial (0 to 1).
    """
    def __init__(self, n: int, p: float):
        if not (0 <= p <= 1):
            raise ValueError("Probability p must be between 0 and 1.")
        self.n = n
        self.p = p
        self.q = 1 - p

    def expected_value(self):
        return self.n * self.p

    def variance(self):
        return self.n * self.p * self.q

    def pmf(self, k: int):
        if not (0 <= k <= self.n):
            return 0
        
        # nCk = n! / (k!(n-k)!)
        combinations = math.comb(self.n, k)
        probability = combinations * (self.p**k) * (self.q**(self.n - k))
        return probability

    def cdf(self, k: int):
        return sum(self.pmf(i) for i in range(k + 1))



def visualize_bernoulli(p):
    
    outcomes = [0, 1]
    probabilities = [1 - p, p]  
    
   
    plt.figure(figsize=(8, 5))
    bars = plt.bar(outcomes, probabilities, color=['#e74c3c', '#2ecc71'], alpha=0.8, edgecolor='black')
    
  
    plt.title(f'Bernoulli Distribution (p = {p})', fontsize=14)
    plt.xlabel('Outcome (X)', fontsize=12)
    plt.ylabel('Probability P(X)', fontsize=12)
    plt.xticks(outcomes, ['0 (Failure)', '1 (Success)']) 
    plt.ylim(0, 1.1) 
    
   
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.02,f'{height:.2f}', ha='center', va='bottom', fontweight='bold')

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


success_probability = 0.5
visualize_bernoulli(success_probability)
 
