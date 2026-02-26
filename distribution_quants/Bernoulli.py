import numpy as np

class Bernoulli:
    def __init__(self, p: float):
        if not (0 <= p <= 1):
            raise ValueError("Parameter p must be in [0, 1]")
        self.p = p
        self.q = 1.0 - p

    def pprobabilty_mass_func(self, k: int) -> float:
        if k == 1:
            return self.p
        elif k == 0:
            return self.q
        return 0.0

    def cummulative_distri_func(self, x: float) -> float:
        if x < 0:
            return 0.0
        elif x < 1:
            return self.q
        return 1.0

    def sample(self, size: int = 1) -> np.ndarray:
        return np.random.binomial(1, self.p, size)

    @property
    def mean(self) -> float:
        return self.p

    @property
    def variance(self) -> float:
        return self.p * self.q

    @property
    def skewness(self) -> float:
        return (self.q - self.p) / np.sqrt(self.p * self.q)

    @property
    def kurtosis(self) -> float:
        return (1 - 6 * self.p * self.q) / (self.p * self.q)
