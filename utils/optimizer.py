from models.optimization_task import OptimizationTask


class Optimizer:
    def __init__(self):
        pass

    def optimize(self, ot: OptimizationTask):
        population = self.generate_initial_population(ot)
        for i in range(ot.config.max_iteration):
            self.crossbending(population, ot)
            self.mutation(ot)
            self.selection(ot)
            self.check_convergence(ot)
            self.plot_results(ot)

    def generate_initial_population(ot: OptimizationTask):
        pass

    def crossbending(population, ot: OptimizationTask):
        pass

    def mutation(ot: OptimizationTask):
        pass

    def selection(ot: OptimizationTask):
        pass

    def check_convergence(ot: OptimizationTask):
        pass

    def plot_results(ot: OptimizationTask):
        pass