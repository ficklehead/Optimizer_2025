from models.optimization_task import *
from models.objective_type import ObjectiveType
from utils.optimizer import Optimizer
from models.design_variable import DesignVariable
from models.objective import Objective
from models.constraint import Constraint


my_task = OptimizationTask()
my_task.cae_models = "D:\\POLITECH_2025\\Optimization\\beam.txt"
my_task.config = OptimizationConfig(5, 0.5, 0.5, 10, 0.001)
my_task.objective = Objective('area', ObjectiveType.MIN,[])
#my_task.constraints.append(Constraint('area', 2, None, []))
my_task.constraints.append(Constraint('def', 0.02, None, []))
my_task.constraints.append(Constraint('stress', 0.05, None, []))
my_task.design_variables.append((DesignVariable('radius_a', 0.9, 0.01, 0.01, [])))
my_task.design_variables.append((DesignVariable('radius_b', 0.9, 0.01, 0.01, [])))
my_task.solver_path = 'D:\\ANSYS24_DOWNLOAD\\ANSYS Inc\\v242\\ANSYS\\bin\\winx64\\ANSYS242.exe'
my_task.work_path = 'D:\\POLITECH_2025\\Optimization'
my_task.solver_script = 'beam'
my_task.results_path = 'D:\\POLITECH_2025\\Optimization\\results.txt'


optimizer = Optimizer()
optimizer.optimize(my_task)