class DesignVariable:
    def __init__(self, name, upper_bound, lower_bound, step, values):
        self.name = name
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        self.step = step
        self.values = values
