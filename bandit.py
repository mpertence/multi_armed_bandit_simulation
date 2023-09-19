import numpy as np

class Bandit:
  def __init__(self, arms, strategy, steps):
    self.arms = arms
    self.strategy = strategy
    self.steps = steps

  def play(self):    
    for step in range(self.steps):
      if step <= 1000:
        arm = np.random.choice(self.arms)
        arm.run()
      else:
        arm = self.strategy.choose(self.arms)
        arm.run()

