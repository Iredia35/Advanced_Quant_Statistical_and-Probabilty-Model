import math

#With just one probability, the bounds are straightforward:
class BonferroniInequality:
    def __init__(self, n: int, A: float) -> float:
        self.n_space = n
        self.probabilityA = A

    def calculate_probability(self):
        sum_individual_probabilities = self.probabilityA * self.n_space
        probability_intersection =  sum_individual_probabilities - (self.n_space - 1) 
        return f"The probability is : {probability_intersection:2f}"
    
    
test = BonferroniInequality(10, 0.99)
print(test.calculate_probability())


#Using the general form of the Bonferroni inequalities, we can analyze multiple events and their probabilities to determine bounds on their intersection and union probabilities.
class BonferroniInequalityGeneral:
    def __init__(self, probabilities):
        
        # Ensure all probabilities are between 0 and 1
        if not all(0 <= p <= 1 for p in probabilities):
            raise ValueError("All probabilities must be between 0 and 1.")
            
        self.probabilities = probabilities
        self.n = len(probabilities)
        self.sum_p = sum(probabilities)

    def intersection_lower_bound(self):
        bound = self.sum_p - (self.n - 1)
        return max(0.0, bound)

    def union_upper_bound(self):
        return min(1.0, self.sum_p)

    def report(self):
        """Prints a summary of the bounds."""
        print(f"Sizing in the  {self.n} events...")
        print(f"Minimum probability all occur: {self.intersection_lower_bound():.4f}")
        print(f"Maximum probability at least one occurs: {self.union_upper_bound():.4f}")


"""
analysis = BonferroniInequalityGeneral([0.95, 0.98, 0.92])

min_all = analysis.intersection_lower_bound()

analysis.report()

"""
