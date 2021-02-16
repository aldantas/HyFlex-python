from py4j.java_gateway import JavaGateway
import random

"""
Hyper Heuristic with Random Selection for the Vehicle Routing Problem
The CHeSC class is only necessary if you want to run your algorithm
in the same conditions of the CHeSC competition
"""

class ExampleHyperHeuristic():
    def __init__(self):
        hyflex = JavaGateway().jvm
        self.problem = hyflex.VRP.VRP(random.randint(0, 10000))
        self.problem.loadInstance(0)
        self.problem.initialiseSolution(0)
        #seed, time limit in milliseconds, problem object
        self.chesc = hyflex.CHeSC(0, 5000, self.problem)
        self.operators = list(range(self.problem.getNumberOfHeuristics()))

    def run(self):
        self.chesc.startTimer()
        current_fitness = self.problem.getFunctionValue(0)
        while not self.chesc.hasRuntimeExpired():
            op = random.choice(self.operators)
            new_fitness = self.problem.applyHeuristic(op, 0, 1)
            delta = current_fitness - new_fitness
            if delta > 0 or random.random() < .5:
                self.problem.copySolution(1, 0)
                current_fitness = new_fitness
        return self.chesc.getBestSolutionValue()


if __name__ == "__main__":
    h = ExampleHyperHeuristic()
    print(h.run())
