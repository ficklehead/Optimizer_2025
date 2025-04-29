from models.optimization_task import OptimizationTask
import numpy as np
import utils.ansys as ansys


class Optimizer:
    def __init__(self):
        pass

    def optimize(self, ot: OptimizationTask):
        population = self.generate_initial_population(ot)
        population_results =  self.calculate_dresps(ot, population)


        for i in range(ot.config.max_iteration):
            children = self.crossbending(population, ot)
            self.mutation(children, ot)
            children_results = self.calculate_dresps(ot, children)
            population, results = self.selection(ot, population, population_results, children, children_results)

            #self.check_convergence(ot)
            ot.objective.values.append(results[0])
            #self.plot_results(ot)
        print(ot.objective.values)

    def generate_initial_population(self, ot: OptimizationTask):
        num_pars = len(ot.design_variables)
        individuals = np.random.rand(ot.config.population_size, num_pars)
        return individuals

    def crossbending(self, population, ot: OptimizationTask):
        children = []
        for i in range(ot.config.population_size):
            parent1 = population[np.random.randint(0, ot.config.population_size)]
            parent2 = population[np.random.randint(0, ot.config.population_size)]
            children.append(np.array([parent1[0], parent2[1]]))
        return np.array(children)


    def mutation(self, children, ot: OptimizationTask):
        for child in children:
            mutation1 = (-1 + np.random.rand() * 2) * 0.1
            mutation2 = (-1 + np.random.rand() * 2) * 0.1
            child = child + np.array([mutation1, mutation2])
            if child[0] < ot.design_variables[0].lower_bound:
                child[0] = ot.design_variables[0].lower_bound
            if child[0] > ot.design_variables[0].upper_bound:
                child[0] = ot.design_variables[0].upper_bound
            if child[1] < ot.design_variables[1].lower_bound:
                child[1] = ot.design_variables[1].lower_bound
            if child[1] > ot.design_variables[1].upper_bound:
                child[1] = ot.design_variables[1].upper_bound

    def selection(self, ot: OptimizationTask, population, population_results, children, children_results):
        results = np.concatenate((children_results.T, population_results.T))
        index_array = np.argsort(results)
        population = np.concatenate((children.T, population.T), axis = 1)
        sorted_population = population.T[index_array]
        sorted_results = results.T[index_array]
        return sorted_population[0:ot.config.population_size], sorted_results[0:ot.config.population_size]


    def check_convergence(self, ot: OptimizationTask):
        pass

    def plot_results(self, ot: OptimizationTask):
        pass

    def change_input(self, individual, ot: OptimizationTask):
        with open(ot.cae_models) as f:
            lines = f.readlines()
        lines[0] = "a="+str(individual[0])+"\n"
        lines[1] = "b="+str(individual[1])+"\n"
        with open(ot.cae_models, "w") as f:
            f.writelines(lines)

    def calculate_dresps(self, ot: OptimizationTask, population):
        results = np.zeros(ot.config.population_size)
        i = 0
        for individual in population:
            self.change_input(individual, ot)
            ansys.runAPDL(ot.solver_path, ot.work_path, ot.solver_script)
            with open(ot.results_path, encoding='utf-8') as f:
                lines = f.readlines()
            results[i] = lines[0]
            i += 1
        return results