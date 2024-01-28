import numpy as np 

class Bandit: 
  def __init__(self, strategy):
    self.arms = []
    self.strategy = strategy

  def add_arm(self,new_arm):
    self.arms.append(new_arm)
    
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

