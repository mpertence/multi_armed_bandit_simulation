from arm import Arm
from bandit import Bandit
from strategy import EpsilonGreedyStrategy, GreedyStrategy, RandomStrategy, UCB

class MaB: 
  def __init__(self, strategy):
    self.strategy = strategy
    self.bandit = 0

  def create_bandit(self):
    self.bandit = Bandit(strategy=self.strategy)
    return self.bandit

  def create_arm(self, name, click_prob, purchase_prob, click_reward=1, purchase_reward=3):
    arm = Arm(name, click_prob, purchase_prob)
    self.bandit.add_arm(arm)

    
  def reset_arms(self):
    for arm in self.arms:
        arm.reset()
        
  def get_total_reward(self):
    total_reward = 0
    for arm in self.arms:
        total_reward += arm.total_reward
    return total_reward

  def get_best_arm(self):
    best_arm_index = np.argmax(self.arms)
    best_arm_instance = self.arms[best_arm_index]
    return best_arm_instance

  def play(self):
    arm = self.strategy.choose(self.arms)
    arm.run()

