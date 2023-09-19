import numpy as np

class EpsilonGreedyStrategy(object):
    """
    ...
    """
    def __init__(self, epsilon):
        self.epsilon = epsilon
    def __str__(self):
        return 'Epsilon-greedy Strategy'
    def choose(self, arms):
        if np.random.rand() < self.epsilon:
            arm = np.random.choice(arms)
            return arm
        else:
            best_arm_index = np.argmax(arms)
            arm = arms[best_arm_index]
            return arm

class GreedyStrategy(EpsilonGreedyStrategy):
    """
    Always the best arm
    """
    def __init__(self):
        super(GreedyStrategy, self).__init__(0)

    def __str__(self):
        return 'greedy'

class RandomStrategy(EpsilonGreedyStrategy):
    """
    Always random arm
    """
    def __init__(self):
        super(RandomStrategy, self).__init__(1)

    def __str__(self):
        return 'greedy'
