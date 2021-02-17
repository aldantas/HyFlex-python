from py4j.java_gateway import JavaGateway
import random
import time

"""
Hyper Heuristic with Random Selection for the Vehicle Routing Problem
The CHeSC class extends the abstract HyperHeuristic class and is necessary
for getting the elapsed CPU time in Java
"""

class ExampleHyperHeuristic():
    def __init__(self):
        hyflex = JavaGateway().jvm
        self.problem = hyflex.VRP.VRP(random.randint(0, 10000))
        self.problem.loadInstance(0)
        #seed, time limit in milliseconds, problem object
        self.time_limit = 5000
        self.chesc = hyflex.CHeSC(0, self.time_limit, self.problem)
        self.operators = list(range(self.problem.getNumberOfHeuristics()))

    def elapsed_time(self, start_time):
        python_elapsed = time.process_time() - start_time
        java_elapsed = self.chesc.getElapsedTime()
        return python_elapsed + java_elapsed

    def run(self):
        self.problem.initialiseSolution(0)
        self.chesc.startTimer()
        start_time = time.process_time()
        current_fitness = self.problem.getFunctionValue(0)
        while self.elapsed_time(start_time) < self.time_limit:
            op = random.choice(self.operators)
            new_fitness = self.problem.applyHeuristic(op, 0, 1)
            delta = current_fitness - new_fitness
            if delta > 0 or random.random() < .5:
                self.problem.copySolution(1, 0)
                current_fitness = new_fitness
        return self.problem.getBestSolutionValue()


if __name__ == "__main__":
    h = ExampleHyperHeuristic()
    print(h.run())
