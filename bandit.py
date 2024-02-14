import numpy as np 

class Bandit: 
    def __init__(self, strategy):
        self.arms = []
        self.strategy = strategy

    def get_best_arm(self):
        best_arm_index = np.argmax(self.arms)
        best_arm_instance = self.arms[best_arm_index]
        return best_arm_instance

    def select_arm_to_run(self, arms):
        arm = self.strategy.choose(arms)
        return arm

