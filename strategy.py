import numpy as np

class EpsilonGreedyStrategy(object):
    """
    ...
    """
    def __init__(self, epsilon):
        self.epsilon = epsilon
        self.avg_reward = 0
    def __str__(self):
        return f'Epsilon-greedy {self.epsilon}'
    
    def choose(self, arms):
        if (np.random.rand() < self.epsilon) or (self.avg_reward == 0):
            arm = np.random.choice(arms)
            self.avg_reward = arm.avg_reward
            return arm
        else:
            best_arm_index = np.argmax(arms)
            arm = arms[best_arm_index]
            self.avg_reward = arm.avg_reward
            return arm

class GreedyStrategy(EpsilonGreedyStrategy):
    """
    Always the best arm
    """
    def __init__(self):
        super(GreedyStrategy, self).__init__(0)

    def __str__(self):
        return 'Greedy'

class RandomStrategy(EpsilonGreedyStrategy):
    """
    Always random arm
    """
    def __init__(self):
        super(RandomStrategy, self).__init__(1)

    def __str__(self):
        return 'Random'
    
class UCB():
    def __init__(self, confidence = 1):
        self._confidence = confidence

    def __str__(self):
        return 'UCB - Upper Confidence Bound'
    
    def get_total_steps(self, arms):
        total_steps = 1
        for arm in arms:
            total_steps += arm.total_views
        
        return total_steps

    def get_arms_stats(self, arms):
        
        arms_stats = [] 
        arm_value = 0
        total_steps = self.get_total_steps(arms)
        
        for arm in arms:
            total_runs = arm.total_views
            arm_avg_reward = arm.avg_reward
            t = total_steps  
            arm_uncertainty = self._confidence * (np.sqrt(np.log(t) / (total_runs + 0.1) ))
            arm_value = arm_avg_reward + arm_uncertainty
            arms_stats.append(arm_value)
        return arms_stats
    
    def choose(self, arms):

        arms_stats = self.get_arms_stats(arms)
        best_arm_index = np.argmax(arms_stats)
        arm = arms[best_arm_index]
        return arm