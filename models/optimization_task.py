from models.optimization_config import OptimizationConfig
from models.objective import Objective
from models.constraint import Constraint
from models.design_variable import DesignVariable
from typing import List


class OptimizationTask:
    def __init__(self, config: OptimizationConfig = None, cae_model=None, objective: Objective = None,
                 constraints: List[Constraint] = [], design_variables: List[DesignVariable] = [], solver_path=None,
                 solver_script=None):
        self.config = config
        self.cae_models = cae_model
        self.objective = objective
        self.constraints = constraints
        self.design_variables = design_variables
        self.solver_path = solver_path
        self.solver_script = solver_script
