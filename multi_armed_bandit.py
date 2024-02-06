from arm import Arm
from bandit import Bandit
from strategy import EpsilonGreedyStrategy, GreedyStrategy, RandomStrategy, UCB

class MaB: 
    def __init__(self, strategy):
        self.bandit = Bandit(strategy)
        self.arms = []
        self.reward_history = []
        self.total_reward_history = []

    def create_arm(self, name, click_prob, purchase_prob, click_reward=1, purchase_reward=3):
        arm = Arm(name, click_prob, purchase_prob)
        self.arms.append(arm)

    def reset_arms(self):
        for arm in self.arms:
            arm.reset()
            
        self.reward_history = []
        
    def get_total_reward(self):
        total_reward = 0
        for arm in self.arms:
            total_reward += arm.total_reward
        return total_reward

    def get_arm_total_reward(self):
        list_to_update = []
        for arm in self.arms:
            list_to_update.append(arm.total_reward)
        self.reward_history.append(list_to_update)
    
    def play(self, number_of_steps):
        bandit = self.bandit
        for step in range(number_of_steps):
            arm = bandit.select_arm_to_run(self.arms)
            arm.run()
            self.get_arm_total_reward()
        
        total_reward = self.get_total_reward()
        self.total_reward_history.append(total_reward)

