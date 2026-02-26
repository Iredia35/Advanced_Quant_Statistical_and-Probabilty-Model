import math 

class GeometricDistribution:
    """
    Geometric Distribution models the number of trials until the first success in a sequence of independent Bernoulli trials.
    
    Parameters:
    - p (float): Probability of success in each trial (0 to 1).
    """
    def __init__(self, p: float):
        if not (0 <= p <= 1):
            raise ValueError("Probability p must be between 0 and 1.")
        self.p = p
        self.q = 1 - p

    def expected_value(self):
        return 1 / self.p

    def variance(self):
        return self.q / (self.p ** 2)

    def pmf(self, k: int):
        if k < 1:
            return 0
        return (self.q ** (k - 1)) * self.p

    def cdf(self, k: int):
        if k < 1:
            return 0
        return 1 - (self.q ** k)
    
class NegativeBinomialDistribution:
    """
    Negative Binomial Distribution models the number of trials until the r-th success in a sequence of independent Bernoulli trials.
    
    Parameters:
    - r (int): Number of successes.
    - p (float): Probability of success in each trial (0 to 1).
    """
    def __init__(self, r: int, p: float):
        if not (0 <= p <= 1):
            raise ValueError("Probability p must be between 0 and 1.")
        self.r = r
        self.p = p
        self.q = 1 - p

    def expected_value(self):
        return self.r / self.p

    def variance(self):
        return self.r * self.q / (self.p ** 2)

    def pmf(self, k: int):
        if k < self.r:
            return 0
        combinations = math.comb(k - 1, self.r - 1)
        probability = combinations * (self.p ** self.r) * (self.q ** (k - self.r))
        return probability

    def cdf(self, k: int):
        if k < self.r:
            return 0
        return sum(self.pmf(i) for i in range(self.r, k + 1))