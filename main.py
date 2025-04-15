from models.optimization_task import *
from models.objective_type import ObjectiveType
from utils.optimizer import Optimizer
from models.design_variable import DesignVariable
from models.objective import Objective
from models.constraint import Constraint


my_task = OptimizationTask()
my_task.cae_models = "D:\\POLITECH_2025\\Optimization\\kirsh.txt"
my_task.config = OptimizationConfig(10, 0.5, 0.5, 20, 0.001)
my_task.objective = Objective('mass', ObjectiveType.MIN,[])
my_task.constraints.append(Constraint('stress', 220e6, None, []))
my_task.design_variables.append((DesignVariable('radius_a', 0.9, 0.1, 0.1, [])))
my_task.design_variables.append((DesignVariable('radius_b', 0.9, 0.1, 0.1, [])))

optimizer = Optimizer()
optimizer.optimize(my_task)