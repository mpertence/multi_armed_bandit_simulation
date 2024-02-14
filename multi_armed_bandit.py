from arm import Arm
from bandit import Bandit
from strategy import EpsilonGreedyStrategy, GreedyStrategy, RandomStrategy, UCB

class MaB: 
    def __init__(self, strategy):
        self.bandit = Bandit(strategy)
        self.arms = []
        self.reward_history = []
        self.purchase_history = []

    def create_arm(self, name, click_prob, purchase_prob, click_reward=1, purchase_reward=3):
        arm = Arm(name, click_prob, purchase_prob)
        self.arms.append(arm)

    def reset_arms(self):
        for arm in self.arms:
            arm.reset()
            
        self.reward_history = []
        self.purchase_history = []
        
    def get_total_reward(self):
        total_reward = 0
        for arm in self.arms:
            total_reward += arm.total_reward
        return total_reward
    
    def update_reward_history(self):
        list_to_update = []
        for arm in self.arms:
            list_to_update.append(arm.total_reward)
        self.reward_history.append(list_to_update)
    
    def get_total_purchase(self):
        total_purchase = 0
        for arm in self.arms:
            total_purchase += arm.total_purchases
        return total_purchase

    def update_purchase_history(self):
        list_to_update = []
        for arm in self.arms:
            list_to_update.append(arm.total_purchases)
        self.purchase_history.append(list_to_update)
    
    def play(self, number_of_steps):
        bandit = self.bandit
        for step in range(number_of_steps):
            arm = bandit.select_arm_to_run(self.arms)
            arm.run()
            self.update_reward_history()
            self.update_purchase_history()

